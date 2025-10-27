# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #53
# "Hipótesis de Markov: Procesos de Markov"

# La "Hipótesis de Markov" (o propiedad de Markov) es
# la suposición de que el futuro es condicionalmente
# independiente del pasado, dado el presente.

# P(X_t+1 | X_t, X_t-1, ..., X_0) = P(X_t+1 | X_t)
#
# "Para predecir el clima de mañana (X_t+1),
#  solo necesito saber el clima de HOY (X_t).
#  No me importa el clima de la semana pasada."
#
# Un "Proceso de Markov" (o Cadena de Markov) es
# un modelo que sigue esta hipótesis.

# --- Ejemplo: Cadena de Markov Simple (Clima) ---
# Estados = {'Sol', 'Lluvia'}
#
# Matriz de Transición T:
# T(i, j) = P(X_t+1 = j | X_t = i)
#
#       Mañana(Sol)  Mañana(Lluvia)
# Hoy(Sol)     0.9           0.1
# Hoy(Lluvia)  0.4           0.6

T = {
    'Sol': {'Sol': 0.9, 'Lluvia': 0.1},
    'Lluvia': {'Sol': 0.4, 'Lluvia': 0.6}
}

# Simulación de un paso:
estado_actual = 'Sol'
print(f"Proceso de Markov (Clima)")
print(f"Hipótesis: El clima de mañana solo depende del de hoy.")
print(f"Matriz de Transición: {T}")
print(f"Estado Actual (t=0): {estado_actual}")

# Simulo t=1
import random
if random.random() < T[estado_actual]['Lluvia']:
    estado_siguiente = 'Lluvia'
else:
    estado_siguiente = 'Sol'
    
print(f"Estado Siguiente (t=1): {estado_siguiente}")
print(f"(La decisión se basó *solo* en '{estado_actual}')")