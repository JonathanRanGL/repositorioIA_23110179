# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #82
# "Gráficos por Computador"

# Es la "inversa" de la Percepción (Visión por Computador).
# Percepción: Imagen -> Modelo (¿Qué es esto?)
# Gráficos: Modelo -> Imagen (¿Cómo se ve esto?)
#
# Es el campo de *generar* imágenes 2D o 3D a partir
# de modelos matemáticos.
#
# --- Pipeline Básico de Renderizado 3D ---
#
# 1. Modelado (Modeling):
#    - Definir la escena: Objetos (mallas de vértices/polígonos),
#      luces, texturas, y una cámara.
#
# 2. Transformación (Transform):
#    - Mover los objetos del "espacio del mundo" al
#      "espacio de la cámara" (vista).
#    - Proyectar la vista 3D a un plano 2D (proyección).
#    - (Todo esto se hace con multiplicación de Matrices 4x4).
#
# 3. Rasterización (Rasterization):
#    - El paso final. Convertir la descripción vectorial 2D
#      (triángulos, líneas) en píxeles en la pantalla.
#    - Calcula el color de cada píxel,
#      considerando texturas, sombras e iluminación.
#
# (Bibliotecas como OpenGL, DirectX, Vulkan, o motores
#  como Unity y Unreal, implementan este pipeline).

print("Gráficos por Computador (Conceptual)")
print("El proceso de crear imágenes a partir de modelos.")
print("\nPipeline 3D Básico:")
print("1. Modelado (Vértices, Triángulos, Luces, Cámara)")
print("2. Transformación (Matrices para mover y proyectar)")
print("3. Rasterización (Convertir triángulos en píxeles)")