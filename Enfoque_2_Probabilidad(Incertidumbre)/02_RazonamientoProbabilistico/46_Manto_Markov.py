# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #46
# "Manto de Markov (Markov Blanket)"

# El "Manto de Markov" de un nodo (X) es el conjunto
# de nodos que lo "aíslan" del resto de la red.
#
# Una vez que *sabemos* los valores del Manto de Markov de X,
# ninguna otra variable en la red nos da información *nueva* sobre X.
#
# El Manto de Markov de X está compuesto por:
# 1. Los Padres de X
# 2. Los Hijos de X
# 3. Los "Co-Padres" de X (es decir, los otros padres de sus hijos)

# --- Ejemplo: Red de Alarma (del Algoritmo 44) ---
#
#    (R)     (T)
#      \       /
#       v     v
#       (Alarma)  <-- Nodo X
#         /   \
#        v     v
#      (J)     (M)
#
# Pregunta: ¿Cuál es el Manto de Markov de "Alarma" (A)?
#
# 1. Padres de A: {Robo, Terremoto}
# 2. Hijos de A: {Juan, María}
# 3. Co-Padres de A: {} (Ni Juan ni María tienen otros padres)
#
# Manto(Alarma) = {Robo, Terremoto, Juan, María}
#
# "Una vez que sé el estado de Robo, Terremoto, Juan y María,
#  ninguna otra variable (si la hubiera) me importa para
#  saber el estado de la Alarma."

# --- Ejemplo 2: Manto de "Robo" (R) ---
#
# 1. Padres de R: {}
# 2. Hijos de R: {Alarma}
# 3. Co-Padres de R: {Terremoto} (T es el otro padre del hijo 'Alarma')
#
# Manto(Robo) = {Alarma, Terremoto}

print("Manto de Markov (Markov Blanket)")
print("Es el conjunto de nodos que 'aíslan' a un nodo X del resto de la red.")
print("\nComposición del Manto(X):")
print("1. Padres(X)")
print("2. Hijos(X)")
print("3. Otros Padres de los Hijos(X) (Co-Padres)")
print("\nEjemplo (Red de Alarma):")
print("Manto(Alarma) = {Robo, Terremoto, Juan, María}")
print("Manto(Robo) = {Alarma, Terremoto}")