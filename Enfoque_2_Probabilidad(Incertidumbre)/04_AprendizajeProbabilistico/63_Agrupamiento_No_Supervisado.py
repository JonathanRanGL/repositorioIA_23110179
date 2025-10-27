# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #63
# "Agrupamiento No Supervisado (Clustering)"

# Es un tipo de Aprendizaje Automático "No Supervisado".
#
# "No Supervisado" significa que los datos de entrenamiento
# *no tienen etiquetas* (no hay una 'y').
#
# El objetivo del "Agrupamiento" (Clustering) es
# encontrar *estructura* oculta en los datos,
# agrupando puntos de datos que son "similares" entre sí.

# --- Características ---
# 1. Datos: Solo X (features).
# 2. Objetivo: Asignar cada punto de X a un grupo (clúster) 'k'.
# 3. Desafío: ¿Qué significa "similar"? ¿Cuántos grupos 'k' hay?

# --- Algoritmos Comunes (ejemplos) ---
#
# 1. k-Medias (k-Means):
#    - Basado en centroides.
#    - Asume que los clústeres son esféricos.
#    - (Ver Algoritmo #65)
#
# 2. Modelos de Mezcla Gaussiana (GMM):
#    - Basado en probabilidad (usa el Algoritmo EM).
#    - Asume que los clústeres son elipses (Gaussianos).
#    - (Ver Algoritmo #62)
#
# 3. DBSCAN (Density-Based):
#    - Basado en densidad.
#    - Encuentra clústeres de formas arbitrarias
#    - No requiere pre-definir el número de clústeres 'k'.

print("Agrupamiento No Supervisado (Clustering)")
print("Objetivo: Encontrar grupos en datos NO etiquetados.")
print("\nDatos de entrada: X (features)")
print("Datos de salida: Una etiqueta de 'grupo' (ej. 0, 1, 2) para cada dato.")
print("\nAlgoritmos principales:")
print(" - k-Medias (k-Means) -> Ver #65")
print(" - Mezcla Gaussiana (GMM) -> Ver #62")
print(" - DBSCAN")