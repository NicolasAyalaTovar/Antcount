"""Antcount: count moving ants in a video using classical computer vision.

The pipeline combines background subtraction (MOG2) with adaptive
thresholding and morphological closing to isolate ants, then filters
contours by area and overlays the live count on each frame.
"""

import argparse
from pathlib import Path

import cv2

DEFAULT_VIDEO = Path(__file__).parent / "data" / "ants_sample.mp4"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect and count ants in a video.")
    parser.add_argument("video", nargs="?", default=str(DEFAULT_VIDEO),
                        help="Path to the input video (default: bundled sample).")
    parser.add_argument("--min-area", type=int, default=500,
                        help="Minimum contour area in pixels to count as an ant (default: 500).")
    return parser.parse_args()


def detect_ants(frame, background_subtractor, min_area: int):
    """Return the contours of the ants detected in a single frame."""
    foreground = background_subtractor.apply(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    combined = cv2.bitwise_and(thresh, foreground)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closed = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [c for c in contours if cv2.contourArea(c) > min_area]


def main() -> None:
    args = parse_args()
    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video: {args.video}")

    background_subtractor = cv2.createBackgroundSubtractorMOG2(
        history=500, varThreshold=16, detectShadows=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        ants = detect_ants(frame, background_subtractor, args.min_area)
        cv2.drawContours(frame, ants, -1, (0, 255, 0), 2)
        cv2.putText(frame, f"Ants: {len(ants)}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("Antcount - press Q to quit", frame)
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
