# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #75
# "Hamming, Hopfield, Hebb, Boltzmann"

# Este es un resumen de varios conceptos y redes
# clásicas, muchas de ellas con interés histórico
# o para aplicaciones específicas (ej. memoria).

print("Resumen de Redes Clásicas y Conceptos:")

print("\n--- 1. Aprendizaje Hebbiano ('Regla de Hebb') ---")
print("  - Concepto (1949): 'Neuronas que disparan juntas,")
print("    se conectan juntas' (Neurons that fire together, wire together).")
print("  - Idea: Si la neurona A y la neurona B están activas")
print("    al mismo tiempo, la conexión (peso) entre ellas")
print("    debe fortalecerse.")
print("  - Es la base de muchos tipos de aprendizaje no supervisado.")

print("\n--- 2. Red de Hopfield ---")
print("  - Tipo: Red Neuronal Recurrente (conexiones bidireccionales).")
print("  - Función: Memoria Asociativa.")
print("  - Se entrena almacenando patrones (vectores).")
print("  - Si se le da un patrón *incompleto* o *ruidoso*,")
print("    la red cae en el estado (patrón almacenado)")
print("    más cercano. (Recuperación de memoria).")

print("\n--- 3. Red de Hamming ---")
print("  - Tipo: Red 'Feed-forward' (hacia adelante).")
print("  - Función: Clasificador simple / Memoria Asociativa.")
print("  - Diseñada para encontrar el patrón almacenado")
print("    que tiene la menor 'Distancia de Hamming'")
print("    (número de bits diferentes) respecto a la entrada.")

print("\n--- 4. Máquina de Boltzmann ---")
print("  - Tipo: Red Neuronal Estocástica (aleatoria) y Recurrente.")
print("  - (Similar a Hopfield, pero con neuronas 'probabilísticas').")
print("  - Usan Temple Simulado (Algoritmo #13) para")
print("    encontrar un equilibrio (optimización).")
print("  - Las 'Máquinas de Boltzmann Restringidas' (RBMs)")
print("    fueron clave en el resurgimiento del Deep Learning.")