# Detector de Hormigas por Visión de Computadora

Este proyecto es un detector de hormigas que utiliza técnicas de visión por computadora para identificar y contar hormigas en un video. El script está desarrollado en Python utilizando OpenCV.

## Descripción

El detector utiliza un sustractor de fondo para distinguir las hormigas en movimiento del fondo estático. Luego, aplica técnicas de procesamiento de imágenes como el desenfoque gaussiano y el umbral adaptativo para mejorar la detección de contornos. Finalmente, dibuja los contornos de las hormigas detectadas y muestra el conteo en el video.

## Requisitos

- Python 3.x
- OpenCV

Puedes instalar OpenCV ejecutando:
```bash
pip install opencv-python

# Autor
Nicolás Ayala Tovar


Este README incluye una descripción del proyecto, instrucciones de uso y la información del autor. Puedes personalizarlo aún más según tus necesidades.