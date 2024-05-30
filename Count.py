import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture("C:/Users/EQUIPO/Documents/Portafolio/python/Video/h.mp4")

    area_minima = 500  

    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        fgmask = fgbg.apply(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        combined = cv2.bitwise_and(thresh, fgmask)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        morphed = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_filtered = [c for c in contours if cv2.contourArea(c) > area_minima]
        frame_contours = frame.copy()
        cv2.drawContours(frame_contours, contours_filtered, -1, (0, 255, 0), 2)

        imagen_con_texto = cv2.putText(frame_contours,
                                       f"Ants: {len(contours_filtered)}",
                                       (10, 50),
                                       cv2.FONT_HERSHEY_SIMPLEX,
                                       1,
                                       (0, 0, 0),  # Color negro
                                       2)

        cv2.imshow("Video con contornos", imagen_con_texto)
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
