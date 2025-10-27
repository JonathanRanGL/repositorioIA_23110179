# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #72
# "Redes Multicapa (Perceptrón Multicapa - MLP)"

# Una Red Multicapa (MLP) resuelve el problema de la
# separabilidad no-lineal (como XOR) al añadir
# una o más "Capas Ocultas" (Hidden Layers) entre
# la entrada y la salida.
#
# (Capa Entrada) -> (Capa Oculta 1) -> (Capa Salida)
#
# Estas capas ocultas, combinadas con funciones de
# activación no-lineales (como ReLU), permiten a la
# red "doblar" el espacio y aprender fronteras
# de decisión complejas.
#
# Se entrenan usando "Retropropagación" (Algoritmo #73).

import numpy as np
from sklearn.neural_network import MLPClassifier

print("Red Multicapa (MLP) resolviendo el problema XOR")

# 1. Datos del problema XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 1, 1, 0]) # Clases (0 o 1)

print("\nDatos X (Entrada):")
print(X)
print("\nDatos y (Salida):")
print(y)

# 2. Inicializar el MLP
# hidden_layer_sizes=(4,): Una capa oculta con 4 neuronas.
# activation='relu': Función de activación (la más común).
# solver='adam': Optimizador (mejor que 'sgd' simple).
# max_iter=1000: Entrenar por más tiempo
model = MLPClassifier(
    hidden_layer_sizes=(4,), 
    activation='relu', 
    solver='adam', 
    max_iter=1000, 
    random_state=42
)

# 3. Entrenar la Red
print("\nEntrenando MLP (usando Backpropagation)...")
model.fit(X, y)

# 4. Predecir
predicciones = model.predict(X)

print(f"\nPredicciones: {predicciones}")
print(f"Reales:       {y}")
print(f"Precisión: {model.score(X, y) * 100:.2f}%")
print("\n¡La Red Multicapa resolvió exitosamente el XOR!")