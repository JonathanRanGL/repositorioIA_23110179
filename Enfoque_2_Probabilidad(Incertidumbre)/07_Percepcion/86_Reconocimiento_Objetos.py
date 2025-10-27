# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #86
# "Reconocimiento de Objetos"

# Es la tarea central de la Visión por Computador.
# Se divide en dos tareas:
#
# 1. Clasificación de Imágenes:
#    "¿Qué hay en esta imagen?" -> "Gato"
#
# 2. Detección de Objetos:
#    "¿Qué hay y *dónde* está?" -> ["Gato", (x, y, w, h)]
#
# --- Enfoques (Evolución) ---
#
# 1. Template Matching (Coincidencia de Plantillas)
#    - Deslizar una imagen "plantilla" (ej. un ojo)
#      sobre la imagen grande y buscar la zona
#      con mayor correlación.
#    - Falla si el objeto cambia de escala, rotación o luz.

print("Reconocimiento de Objetos (Conceptual)")
print("Tareas: 1. Clasificación (¿Qué?) 2. Detección (¿Qué y Dónde?)")
print("\n--- 1. Enfoque Clásico (Template Matching) ---")
print("  - Deslizar una plantilla. Rígido, falla con cambios.")

# 2. Enfoque Clásico (Features + Clasificador)
#    - Paso A (Features): Extraer "features" robustas
#      (SIFT, SURF, HOG - Histogram of Oriented Gradients).
#    - Paso B (Clasificador): Entrenar un clasificador
#      (ej. SVM, Algoritmo #66) con esas features.
#    - (El clasificador de caras Viola-Jones usa
#      features 'Haar' y un 'AdaBoost'.)
print("\n--- 2. Enfoque Clásico (Features + SVM/Boost) ---")
print("  A. Extraer Features (HOG, SIFT).")
print("  B. Entrenar un Clasificador (SVM) con las features.")

# 3. Enfoque Moderno (Deep Learning)
#    - Redes Neuronales Convolucionales (CNNs).
#    - La red "aprende" las features y el clasificador
#      al mismo tiempo (End-to-End).
#    - Clasificación: (AlexNet, VGG, ResNet)
#    - Detección: (R-CNN, YOLO, SSD)
print("\n--- 3. Enfoque Moderno (Deep Learning) ---")
print("  - Redes Convolucionales (CNNs).")
print("  - Aprenden las features automáticamente.")
print("  - Detección: YOLO, SSD, R-CNN.")