# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #84
# "Detección de Aristas y Segmentación"

import numpy as np
import cv2

# --- 1. Detección de Aristas (Edges) ---
#
# Es la tarea de encontrar "discontinuidades" abruptas
# en la intensidad de los píxeles (cambios de color/brillo).
# (Ej. El borde entre una mesa y la pared).
#
# El algoritmo más famoso es "Canny Edge Detector".
# Pasa por 4 etapas:
# 1. Suavizado (Gaussian Blur) para quitar ruido.
# 2. Gradientes (Sobel) para encontrar la "fuerza" y
#    "dirección" del borde.
# 3. Supresión de No-Máximos (adelgaza los bordes).
# 4. Umbralización por Histéresis (conecta bordes débiles a fuertes).

print("1. Detección de Aristas (Canny)")
# 1. Crear una imagen de un cuadrado
image = np.zeros((100, 100), dtype=np.uint8)
image[25:75, 25:75] = 255 # Cuadrado blanco en fondo negro

# 2. Aplicar Canny
# (50 y 150 son los umbrales de histéresis)
edges = cv2.Canny(image, 50, 150)

print(f"Imagen original (cuadrado) shape: {image.shape}")
print(f"Imagen de aristas (bordes) shape: {edges.shape}")
# Los bordes solo tendrán píxeles (255) donde
# Canny encontró una arista.
print(f"Píxeles 'activos' en la imagen de aristas: {np.count_nonzero(edges)}")


# --- 2. Segmentación ---
#
# Es la tarea de "particionar" la imagen en regiones.
# El objetivo es agrupar píxeles que pertenecen
# al mismo objeto.
# (Ej. Asignar 'Clase 0' a todos los píxeles del cielo,
#  'Clase 1' al pasto, 'Clase 2' a la vaca).
#
# Métodos:
# 1. Basados en Umbral (Thresholding):
#    (Píxeles > 128 son 'Objeto', < 128 son 'Fondo')
# 2. Basados en Aristas:
#    (Las aristas de Canny forman el contorno del objeto)
# 3. Basados en Regiones (Clustering):
#    (k-Means aplicado a los colores de los píxeles)
# 4. Deep Learning (U-Net, Mask R-CNN):
#    (El método moderno más preciso)

print("\n\n2. Segmentación (Conceptual)")
print("Tarea: Particionar la imagen en objetos o regiones.")
print("Ejemplo: 'Estos 5000 píxeles son el gato',")
print("         'estos 10000 píxeles son el fondo'.")
print("Métodos: Umbralización, k-Means (color), Deep Learning (U-Net).")