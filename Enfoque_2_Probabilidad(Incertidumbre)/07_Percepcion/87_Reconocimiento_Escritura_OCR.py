# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #87
# "Reconocimiento de Escritura (OCR)"

# El Reconocimiento Óptico de Caracteres (OCR)
# es la tarea de convertir imágenes de texto
# (escaneado o fotografiado) en texto editable.

print("Reconocimiento Óptico de Caracteres (OCR)")
print("Tarea: Convertir imagen de texto -> texto digital.")

# --- Pipeline de un OCR Clásico ---
#
# 1. Preprocesado:
#    - Binarización: Convertir a blanco y negro (Umbral de Otsu).
#    - Eliminación de ruido (De-skewing): Enderezar la página.
#
# 2. Segmentación:
#    - Encontrar líneas de texto.
#    - Encontrar palabras (basado en espacios).
#    - Encontrar caracteres (separar letras pegadas).
#
# 3. Reconocimiento (Clasificación):
#    - Para cada imagen de caracter, clasificarla.
#    - (Ej. "¿Esta imagen es una 'a', 'b', 'c', ...?")
#    - (Se usaban SVMs o k-NN sobre features (HOG)).
#
# 4. Post-procesado (Modelo de Lenguaje):
#    - Corregir errores usando un modelo de lenguaje (n-grama).
#    - (Si el OCR leyó "holq", el modelo sabe que
#      P("hola") > P("holq") y lo corrige).

print("\n--- Pipeline Clásico ---")
print("1. Preprocesado (Binarización, enderezar)")
print("2. Segmentación (Líneas -> Palabras -> Caracteres)")
print("3. Reconocimiento (Clasificar cada imagen de caracter)")
print("4. Post-procesado (Corregir errores con Modelo de Lenguaje)")

# --- Enfoque Moderno (Deep Learning) ---
#
# Se usan Redes Neuronales Recurrentes (LSTM) junto
# con Convolucionales (CNNs).
# (Ej. Tesseract 4+, Google Lens).
#
# 1. Una CNN extrae features de "franjas" de la imagen.
# 2. Una RNN (LSTM) "lee" la secuencia de features
#    y decodifica la secuencia de caracteres.
#
# (Esto evita la segmentación frágil de caracteres).

print("\n--- Enfoque Moderno (LSTM + CNN) ---")
print("Una CNN extrae features y una RNN (LSTM) 'lee' la")
print("secuencia de features para generar el texto.")
print("(Bibliotecas: Tesseract, EasyOCR)")