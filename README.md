# 🐜 Antcount

**Detección y conteo automático de hormigas en video mediante visión por computadora.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)

Antcount procesa un video cuadro a cuadro, identifica las hormigas en movimiento y muestra en pantalla su contorno y el conteo en tiempo real. Está pensado como herramienta de apoyo para estudios de comportamiento y actividad de forrajeo en entomología.

## ⚙️ Cómo funciona

| Etapa | Técnica | Propósito |
|---|---|---|
| 1 | Sustracción de fondo (MOG2) | Separar objetos en movimiento del fondo estático |
| 2 | Desenfoque gaussiano + umbral adaptativo | Resaltar los cuerpos oscuros de las hormigas |
| 3 | Intersección de máscaras + cierre morfológico | Unir regiones y eliminar ruido |
| 4 | Filtrado de contornos por área | Descartar detecciones demasiado pequeñas |
| 5 | Anotación del cuadro | Dibujar contornos y mostrar el conteo |

## 🚀 Instalación

```bash
git clone https://github.com/NicolasAyalaTovar/Antcount.git
cd Antcount
pip install -r requirements.txt
```

## ▶️ Uso

Con el video de ejemplo incluido:

```bash
python antcount.py
```

Con un video propio y un área mínima personalizada:

```bash
python antcount.py ruta/al/video.mp4 --min-area 300
```

Pulsa **Q** para cerrar la ventana.

| Parámetro | Descripción | Valor por defecto |
|---|---|---|
| `video` | Ruta del video de entrada | `data/ants_sample.mp4` |
| `--min-area` | Área mínima (px) para contar un contorno como hormiga | `500` |

## 📁 Estructura

```
Antcount/
├── antcount.py          # Script principal
├── data/
│   └── ants_sample.mp4  # Video de ejemplo
└── requirements.txt
```

## 🔭 Mejoras futuras

- Seguimiento individual (tracking) para evitar contar dos veces la misma hormiga.
- Exportar el conteo por cuadro a CSV para análisis posterior.
- Calibración automática de `--min-area` según la resolución del video.

## 👤 Autor

**Nicolás Ayala Tovar** · [GitHub](https://github.com/NicolasAyalaTovar)
