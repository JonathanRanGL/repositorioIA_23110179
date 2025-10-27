# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #85
# "Texturas y Sombras"

# --- 1. Texturas ---
#
# La textura es una medida de la "apariencia" de una
# superficie (suave, rugosa, rayada, punteada).
#
# En visión por computador, la textura es un patrón
# repetitivo de intensidades de píxeles.
#
# Análisis de Textura:
# Es la tarea de "describir" esta textura con un
# vector de números (un "descriptor").
#
# Métodos:
# - Filtros de Gabor: Miden la respuesta de la imagen
#   a diferentes frecuencias y orientaciones (como
#   en la corteza visual humana).
# - Patrones Binarios Locales (LBP): Un descriptor
#   muy rápido que compara un píxel con sus vecinos.
# - (Moderno): Redes Convolucionales (CNNs) que
#   aprenden los descriptores de textura automáticamente.

print("--- 1. Texturas (Conceptual) ---")
print("Descripción: Patrones repetitivos de intensidad (rugoso, suave).")
print("Objetivo: Crear un 'descriptor' (vector) de la textura.")
print("Métodos: Filtros de Gabor, LBP (Patrones Binarios Locales), CNNs.")

# --- 2. Sombras (Shape from Shading) ---
#
# Es la tarea de inferir la *forma 3D* de un objeto
# a partir de cómo la luz y las sombras caen sobre él.
#
# El cerebro humano es experto en esto: vemos las
# sombras en una foto de una cara e inferimos la
# forma de la nariz, los pómulos, etc.
#
# Problema: Es muy difícil (mal condicionado).
# Múltiples formas 3D pueden producir la misma sombra
# si la luz se mueve.
#
# Métodos:
# - Clásico: Resuelve ecuaciones diferenciales (Reflectancia
#   Lambertiana) asumiendo una fuente de luz y
#   una superficie suave.
# - Múltiples Luces (Photometric Stereo):
#   Se toman 3+ fotos del objeto (quieto) con 3+
#   luces desde diferentes ángulos. Esto da suficiente
#   información para resolver la "normal" (orientación 3D)
#   de cada píxel.

print("\n--- 2. Sombras (Shape from Shading) ---")
print("Descripción: Inferir la forma 3D a partir de las sombras.")
print("Problema: Muy difícil (mal condicionado).")
print("Solución (Photometric Stereo):")
print("  - Tomar 3+ fotos con 3+ luces diferentes.")
print("  - Resolver la orientación (normal) 3D para cada píxel.")