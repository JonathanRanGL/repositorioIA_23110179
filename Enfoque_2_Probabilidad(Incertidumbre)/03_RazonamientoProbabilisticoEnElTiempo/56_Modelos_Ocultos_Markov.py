# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #56
# "Modelos Ocultos de Markov (HMM)"

# Un HMM es un Proceso de Markov donde los estados
# no se observan directamente.
#
# El estado (X_t) está "oculto".
# Solo vemos una "observación" (E_t) que depende del estado.
#
# (X_t-1) --> (X_t) --> (X_t+1)  (Cadena de Markov Oculta)
#    |           |          |
#    v           v          v
#  (E_t-1)     (E_t)      (E_t+1)  (Observaciones)

# --- Componentes de un HMM ---

# 1. Estados (Ocultos), S
# (Ej. 'Lluvia', 'Sol')
S = {'Lluvia', 'Sol'}

# 2. Observaciones (Visibles), O
# (Ej. 'Paraguas', 'No Paraguas')
O = {'Paraguas', 'No Paraguas'}

# 3. Probabilidades Iniciales, P(X_0)
# (Ej. {Lluvia: 0.5, Sol: 0.5})
P_X0 = {'Lluvia': 0.5, 'Sol': 0.5}

# 4. Modelo de Transición, T = P(X_t | X_t-1)
# (La Cadena de Markov)
T = {
    # P(X_t | X_t-1 = 'Lluvia')
    'Lluvia': {'Lluvia': 0.7, 'Sol': 0.3},
    # P(X_t | X_t-1 = 'Sol')
    'Sol': {'Lluvia': 0.2, 'Sol': 0.8}
}

# 5. Modelo de Observación (o Emisión), E = P(E_t | X_t)
# (El "sensor" que conecta lo oculto con lo visible)
E = {
    # P(E_t | X_t = 'Lluvia')
    'Lluvia': {'Paraguas': 0.9, 'No Paraguas': 0.1},
    # P(E_t | X_t = 'Sol')
    'Sol': {'Paraguas': 0.1, 'No Paraguas': 0.9}
}

print("Modelo Oculto de Markov (HMM)")
print("Define un sistema con un estado oculto (X)")
print("y una observación visible (E).")
print("\nComponentes:")
print(f"1. Estados Ocultos (S): {S}")
print(f"2. Observaciones (O): {O}")
print(f"3. P. Inicial P(X_0): {P_X0}")
print(f"4. Modelo de Transición P(X_t | X_t-1): {T}")
print(f"5. Modelo de Observación P(E_t | X_t): {E}")
print("\nLas tareas (Filtrado, Suavizado, etc.) usan este modelo.")