# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #68
# "Computación Neuronal (Concepto)"

# La computación neuronal se basa en un modelo
# simplificado de una neurona biológica: el "Perceptrón".

# Modelo de una Neurona Artificial:
#
# 1. Entradas (Inputs): (x1, x2, x3)
#    (Representan las 'dendritas', los datos de entrada)
#
# 2. Pesos (Weights): (w1, w2, w3)
#    (Representan la 'fuerza' de cada sinapsis.
#     Estos son los parámetros que el modelo *aprende*).
#
# 3. Suma Ponderada:
#    z = (x1 * w1) + (x2 * w2) + (x3 * w3) + b (bias)
#    (El 'sesgo' (bias) 'b' es un umbral de activación)
#
# 4. Función de Activación:
#    y = f(z)
#    (Una función no-lineal (ej. Sigmoid, ReLU) que
#     'dispara' la neurona si la suma es lo bastante alta).
#
# 5. Salida (Output): y
#    (Representa el 'axón', el resultado de la neurona)

print("Computación Neuronal (Modelo de Neurona Artificial)")
print("\n   [x1] --(w1)-->\n")
print("   [x2] --(w2)--> [Suma (z) + bias (b)] -> [f(z)] -> (y) Salida\n")
print("   [x3] --(w3)-->\n")
print("\nEl 'aprendizaje' consiste en encontrar los pesos (w) y")
print("el sesgo (b) correctos usando un algoritmo como")
print("la Retropropagación del Error (Backpropagation).")