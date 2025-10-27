# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #64
# "Modelos de Markov Ocultos (Aprendizaje)"

# El "Aprendizaje" en HMMs (ver Algoritmo #56) se refiere
# a cómo encontrar los parámetros del modelo (T y E)
# cuando solo tenemos las secuencias de observaciones (E_t).
#
# Este es un problema de "variable latente" (el estado X_t está oculto),
# por lo que se resuelve con una versión del Algoritmo EM
# llamada "Algoritmo de Baum-Welch".

# Usaremos la biblioteca 'hmmlearn' para demostrarlo.

from hmmlearn import hmm
import numpy as np

# 1. Datos de Observación
# Supongamos 3 secuencias de observaciones
# (ej. 0=No Paraguas, 1=Paraguas)
O_seq1 = np.array([[0], [0], [1], [1], [0]])
O_seq2 = np.array([[0], [1], [1], [0]])
O_seq3 = np.array([[0], [0], [0], [1]])
# Juntamos los datos
X_data = np.concatenate([O_seq1, O_seq2, O_seq3])
X_lengths = [len(O_seq1), len(O_seq2), len(O_seq3)]

print("Aprendizaje de Parámetros de HMM (Baum-Welch / EM)")
print(f"Datos: {X_data.ravel()}")
print(f"Longitudes: {X_lengths}")

# 2. Inicializar el HMM
# n_components = número de estados ocultos (ej. 2: Sol, Lluvia)
# n_iter = cuántas veces correr EM (Baum-Welch)
model = hmm.MultinomialHMM(n_components=2, n_iter=100, random_state=42)

# 3. Entrenar el Modelo (Aprender los parámetros)
# Esto ejecuta el algoritmo de Baum-Welch (EM)
print("\nEntrenando HMM (Aprendiendo T y E)...")
model.fit(X_data, X_lengths)

# 4. Ver Parámetros Aprendidos
print("\n¡Parámetros aprendidos!")

# P(X_0)
print("P. Iniciales P(X_0):")
print(model.startprob_.round(3))

# T = P(X_t | X_t-1)
print("\nMatriz de Transición (T):")
print(model.transmat_.round(3))

# E = P(E_t | X_t)
print("\nMatriz de Emisión (E):")
print(model.emissionprob_.round(3))
# (Fila 0 = P(Observación | Estado Oculto 0))
# (Fila 1 = P(Observación | Estado Oculto 1))