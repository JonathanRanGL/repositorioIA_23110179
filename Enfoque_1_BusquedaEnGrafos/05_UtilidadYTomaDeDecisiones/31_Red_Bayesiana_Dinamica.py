# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #31
# "Red Bayesiana Dinámica (DBN) - Concepto"

# Una DBN modela cómo las variables (el estado del mundo)
# cambian a lo largo del tiempo.
# Es una Red Bayesiana "desenrollada" en el tiempo.
#
# (t) -------> (t+1)
#
# (Clima_t) --> (Clima_t+1)
#    |             |
# (Paraguas_t)   (Paraguas_t+1)
#
# Un MDP y un POMDP son tipos específicos de DBNs.

# --- Tarea de Ejemplo: Filtrado (Forward Pass) ---
#
# Objetivo: Calcular P(Estado_t+1 | Evidencia_t)
#
# Modelo:
# P(Clima_t+1 | Clima_t)  (Modelo de Transición)
# P(Paraguas_t | Clima_t) (Modelo de Sensor/Evidencia)
#
# P(Clima_0) = {Lluvia: 0.5, Sol: 0.5} (Creencia inicial)

# 1. Modelo de Transición P(Clima_t+1 | Clima_t)
# Si llueve hoy, 70% de prob. de que llueva mañana.
# Si hace sol hoy, 90% de prob. de que haga sol mañana.
T = {
    'Lluvia': {'Lluvia': 0.7, 'Sol': 0.3},
    'Sol':    {'Lluvia': 0.1, 'Sol': 0.9}
}

# 2. Creencia Inicial P(Clima_0)
P_t0 = {'Lluvia': 0.5, 'Sol': 0.5}
print(f"DBN: Tarea de Filtrado (Predicción)")
print(f"Creencia inicial P(Clima_0): {P_t0}")

# --- Paso 1: Predicción (Calcular P(Clima_1) *antes* de observar) ---
# P(Clima_t+1) = SUMA [ P(Clima_t+1 | Clima_t) * P(Clima_t) ]
#                (sobre todos los estados de Clima_t)

P_t1_pred = {'Lluvia': 0.0, 'Sol': 0.0}

# P(Clima_1=Lluvia) = P(C1|C0=Lluvia)*P(C0=Lluvia) + P(C1|C0=Sol)*P(C0=Sol)
P_t1_pred['Lluvia'] = (T['Lluvia']['Lluvia'] * P_t0['Lluvia']) + \
                      (T['Sol']['Lluvia'] * P_t0['Sol'])
# P_t1_pred['Lluvia'] = (0.7 * 0.5) + (0.1 * 0.5) = 0.35 + 0.05 = 0.40

# P(Clima_1=Sol) = P(C1|C0=Lluvia)*P(C0=Lluvia) + P(C1|C0=Sol)*P(C0=Sol)
P_t1_pred['Sol'] = (T['Lluvia']['Sol'] * P_t0['Lluvia']) + \
                   (T['Sol']['Sol'] * P_t0['Sol'])
# P_t1_pred['Sol'] = (0.3 * 0.5) + (0.9 * 0.5) = 0.15 + 0.45 = 0.60

print(f"Predicción P(Clima_1) (antes de evidencia): {P_t1_pred}")

# --- Paso 2: Actualización (Incorporar Evidencia) ---
#
# Observamos que en t=1, alguien usó un paraguas (E1 = 'Paraguas').
#
# 3. Modelo de Sensor/Evidencia P(Evidencia_t | Clima_t)
# P(Paraguas | Lluvia) = 0.9
# P(Paraguas | Sol) = 0.2
E = {
    'Lluvia': 0.9,
    'Sol': 0.2
}

# P(Clima_1 | E1) = alfa * P(E1 | Clima_1) * P(Clima_1)
# (Usamos P_t1_pred que calculamos antes)

P_t1_actual = {'Lluvia': 0.0, 'Sol': 0.0}
total_prob = 0 # (alfa)

# Cálculo (sin normalizar)
P_t1_actual['Lluvia'] = E['Lluvia'] * P_t1_pred['Lluvia'] # 0.9 * 0.40 = 0.36
P_t1_actual['Sol'] = E['Sol'] * P_t1_pred['Sol']       # 0.2 * 0.60 = 0.12
total_prob = P_t1_actual['Lluvia'] + P_t1_actual['Sol'] # 0.36 + 0.12 = 0.48

# Normalización
P_t1_actual['Lluvia'] = P_t1_actual['Lluvia'] / total_prob # 0.36 / 0.48 = 0.75
P_t1_actual['Sol'] = P_t1_actual['Sol'] / total_prob     # 0.12 / 0.48 = 0.25

print(f"Evidencia en t=1: 'Paraguas'")
print(f"Creencia actualizada P(Clima_1 | Evidencia): {P_t1_actual}")