# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #67
# "Aprendizaje Profundo (Deep Learning)"

# El Aprendizaje Profundo es un subcampo del Aprendizaje Automático
# basado en "Redes Neuronales Artificiales (ANNs)".
#
# "Profundo" (Deep) se refiere a que la red neuronal
# tiene *múltiples capas* ocultas (hidden layers).
# (Un Perceptrón simple no es "profundo").
#
# La característica clave es que estas redes aprenden
# "representaciones" (features) de los datos de forma
# automática y jerárquica.
#
# Ej. En visión (CNNs):
# Capa 1 aprende: Bordes simples, esquinas.
# Capa 2 aprende: Combinaciones (círculos, cuadrados).
# Capa 3 aprende: Partes de objetos (ojos, narices).
# Capa 4 aprende: Objetos completos (caras).
#
# Esto elimina la necesidad de "Ingeniería de Features" manual.

print("Aprendizaje Profundo (Deep Learning)")
print("Es aprendizaje automático usando Redes Neuronales")
print("con múltiples capas (profundas).")

print("\nArquitecturas Clave:")
print("1. Redes Neuronales Artificiales (ANNs) / Perceptrón Multicapa (MLP):")
print("   - Capas 'Densas' (totalmente conectadas).")
print("   - Bueno para datos tabulares, clasificación simple.")
print("   - (Se verán en el bloque 2.5)")

print("\n2. Redes Neuronales Convolucionales (CNNs):")
print("   - Usan capas de 'Convolución' (filtros).")
print("   - Dominantes en Visión por Computador (imágenes, video).")
print("   - Capturan jerarquías espaciales (bordes -> formas -> objetos).")

print("\n3. Redes Neuronales Recurrentes (RNNs) / LSTMs / GRUs:")
print("   - Tienen 'memoria' (conexiones que vuelven hacia atrás).")
print("   - Dominantes en datos secuenciales (texto, series de tiempo, audio).")
print("   - (Ej. Reconocimiento del Habla, Traducción).")

print("\n4. Transformers (Auto-Atención):")
print("   - Arquitectura moderna (ej. BERT, GPT).")
print("   - Reemplazando a las RNNs en Procesamiento de Lenguaje.")

print("\nEntrenamiento: Se usa 'Retropropagación' (Backpropagation). (Ver #56)")