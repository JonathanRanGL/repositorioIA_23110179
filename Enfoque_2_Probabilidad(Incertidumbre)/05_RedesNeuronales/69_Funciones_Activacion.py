# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #69
# "Funciones de Activación"

# La función de activación introduce no-linealidad en la red,
# permitiéndole aprender relaciones complejas (como XOR).
# Sin ellas, una red neuronal profunda sería solo una
# gran regresión lineal.

import numpy as np

# Rango de entrada (z)
z = np.array([-5.0, -2.0, -1.0, 0.0, 1.0, 2.0, 5.0])
print(f"Valores de entrada (z): {z}")

# --- 1. Sigmoid ---
# Comprime los números al rango (0, 1).
# Usada en capas de salida para clasificación binaria (Probabilidad).
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
print(f"\n1. Sigmoid (rango 0 a 1):\n   {sigmoid(z).round(3)}")

# --- 2. Tangente Hiperbólica (tanh) ---
# Comprime los números al rango (-1, 1).
# A menudo preferida sobre sigmoid en capas ocultas.
def tanh(z):
    return np.tanh(z)
print(f"\n2. Tanh (rango -1 a 1):\n   {tanh(z).round(3)}")

# --- 3. Unidad Lineal Rectificada (ReLU) ---
# f(z) = max(0, z). Es la más popular en capas ocultas.
# Es muy rápida computacionalmente y evita
# problemas de "desvanecimiento de gradiente".
def relu(z):
    return np.maximum(0, z)
print(f"\n3. ReLU (rango 0 a infinito):\n   {relu(z).round(3)}")

# --- 4. (Step Function) ---
# Usada por el Perceptrón original. No es diferenciable,
# por lo que no se usa con backpropagation.
def step_function(z):
    return np.where(z >= 0, 1, 0)
print(f"\n4. Step (Escalón) (0 o 1):\n   {step_function(z).round(3)}")