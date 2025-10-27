# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #83
# "Preprocesado: Filtros"

# El preprocesado es el primer paso en Percepción:
# limpiar y preparar la imagen para tareas posteriores.
#
# Los "Filtros" son la herramienta principal. Un filtro
# (o 'kernel') es una pequeña matriz que se "desliza"
# sobre la imagen para modificarla.
#
# Filtro de Suavizado (Blurring):
# Se usa para *eliminar ruido* (ej. ruido Gaussiano).
# El filtro promedia los píxeles vecinos.
# (Ej. Filtro Gaussiano, Filtro de Mediana).

import numpy as np
import cv2 # Biblioteca OpenCV

# 1. Crear una imagen de "ruido" (sin cargar un archivo)
# (Imagen 100x100 de "sal y pimienta")
noisy_image = np.zeros((100, 100), dtype=np.uint8)
# Añadir ruido aleatorio
noise = np.random.randint(0, 100, (100, 100))
noisy_image[noise < 10] = 0   # Pimienta
noisy_image[noise > 90] = 255 # Sal

print("Preprocesado: Filtros (con OpenCV)")
print(f"Imagen original (ruidosa) shape: {noisy_image.shape}")
print(f"  Media de intensidad (ruidosa): {np.mean(noisy_image):.2f}")

# 2. Aplicar un Filtro de Suavizado (Gaussian Blur)
# (ksize=(5, 5) es el tamaño del kernel del filtro)
# (sigmaX=0 le dice a OpenCV que calcule la desv. estándar)
blurred_image = cv2.GaussianBlur(noisy_image, ksize=(5, 5), sigmaX=0)

print(f"\nImagen filtrada (suavizada) shape: {blurred_image.shape}")
print(f"  Media de intensidad (suavizada): {np.mean(blurred_image):.2f}")
print("\n(El filtro 'promedió' el ruido blanco y negro,")
print(" acercando la media de la imagen a gris.)")

# (En una app real, mostrarías la imagen con cv2.imshow())