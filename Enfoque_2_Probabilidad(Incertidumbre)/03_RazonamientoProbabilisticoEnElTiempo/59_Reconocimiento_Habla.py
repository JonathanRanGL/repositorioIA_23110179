# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #59
# "Reconocimiento del Habla"

# El Reconocimiento Automático del Habla (ASR)
# es la tarea de convertir una señal de audio (onda sonora)
# en una secuencia de palabras (texto).

# --- Enfoque Clásico (Basado en HMM) ---
# Este es el motivo por el que está en esta sección.
# El problema se modela como una tarea de HMM.
#
# Queremos encontrar la secuencia de palabras 'W' más probable
# dada la secuencia de audio 'A'.
# P(W | A)
#
# Por Bayes: P(W|A) = alfa * P(A|W) * P(W)
#
# 1. Modelo Acústico: P(A | W)
#    (Prob. de escuchar 'A' si se dijo 'W')
#    - Esto es un HMM.
#    - Estados Ocultos (X): Fonemas (ej. 'a', 'b', 'k')
#    - Observaciones (E): Tramas de audio (Vectores MFCC)
#    - P(E | X) = Modelo de Emisión (usualmente un GMM)
#    - P(X_t | X_t-1) = Modelo de Transición (fonemas)
#
# 2. Modelo de Lenguaje: P(W)
#    (Prob. de que la secuencia 'W' sea dicha)
#    (Ej. P("hola mundo") > P("hola mantis"))
#    - Usualmente un "n-grama" (ej. P(mundo | hola))
#
# El algoritmo de "Explicación" (Viterbi) encuentra
# la secuencia de estados (fonemas/palabras) más
# probable que explique las observaciones (audio).

# --- Enfoque Moderno (Deep Learning) ---
# Redes Neuronales Recurrentes (RNN), LSTMs o Transformers
# que aprenden la conversión "End-to-End" (de audio a texto)
# directamente, a menudo sin HMMs explícitos.

print("Reconocimiento del Habla (ASR)")
print("Tarea: Convertir audio -> texto.")
print("\nEnfoque Clásico (HMM):")
print("  Encontrar W que maximiza P(A|W) * P(W)")
print("\n  1. Modelo Acústico P(A|W):")
print("     - HMM donde los estados son Fonemas")
print("     - y las observaciones son Tramas de Audio (MFCCs).")
print("\n  2. Modelo de Lenguaje P(W):")
print("     - Probabilidad 'a priori' de una secuencia de palabras (n-gramas).")
print("\n  El Algoritmo de Viterbi encuentra la secuencia de palabras más probable.")
print("\nEnfoque Moderno: Deep Learning (RNNs, Transformers).")