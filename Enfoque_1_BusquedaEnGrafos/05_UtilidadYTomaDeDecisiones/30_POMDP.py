# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #30
# "MDP Parcialmente Observable (POMDP) - Concepto"

# Un POMDP es un MDP donde el agente *no sabe* en qué estado
# está exactamente.
#
# Ejemplo: Un robot en un laberinto puede estar en (0,1) o (0,2),
# pero su sensor (Observación) solo dice "Veo una pared".
#
# El agente mantiene un "Estado de Creencia" (Belief State),
# que es una distribución de probabilidad sobre los estados.
# b(s) = "Creo que hay un 70% de prob. de estar en s1 y 30% en s2"

# Un POMDP añade 2 componentes a un MDP:
# 6. Omega: Conjunto de Observaciones
#    (Lo que los sensores pueden "ver")
# 7. O: Modelo de Observación (Probabilidad)
#    O(o | s')
#    "La probabilidad de *ver* la observación 'o',
#     dado que *realmente* estoy en el estado s' (siguiente)."

# --- Simulación de un "Paso de Actualización de Creencia" ---
#
# Estados: S = {s1 (Lluvia), s2 (Sol)}
# Acción: a = "ObservarCielo"
# Observaciones: Omega = {o1 (Nublado), o2 (Despejado)}

# 1. Creencia Inicial b(s)
b = {'s1': 0.5, 's2': 0.5} # "No tengo idea"

# 2. Modelo de Transición P(s' | s, a)
# (Asumimos que 'ObservarCielo' no cambia el clima)
P = {
    's1': {'ObservarCielo': [('s1', 1.0), ('s2', 0.0)]},
    's2': {'ObservarCielo': [('s1', 0.0), ('s2', 1.0)]}
}

# 3. Modelo de Observación O(o | s')
# P( ver 'Nublado' | estado es 'Lluvia' ) = 0.8
# P( ver 'Despejado' | estado es 'Lluvia' ) = 0.2
# P( ver 'Nublado' | estado es 'Sol' ) = 0.3
# P( ver 'Despejado' | estado es 'Sol' ) = 0.7
O = {
    's1': {'o1': 0.8, 'o2': 0.2},
    's2': {'o1': 0.3, 'o2': 0.7}
}

# --- El Agente toma la acción a='ObservarCielo' y ve o='Nublado' (o1) ---
# ¿Cuál es su *nueva* creencia b'(s)?

print(f"POMDP: Actualización de Creencia")
print(f"Creencia inicial b(s): {b}")

a = 'ObservarCielo'
o = 'o1' # Vimos 'Nublado'
print(f"Acción: {a}, Observación: {o}")

b_new = {}
total_prob = 0 # Para normalizar (alfa)

# b'(s') = alfa * O(o | s') * SUMA [ P(s' | s, a) * b(s) ]
for s_prime in ['s1', 's2']: # s'
    
    # O(o | s')
    prob_obs = O[s_prime][o]
    
    # SUMA [ P(s' | s, a) * b(s) ] (Predicción)
    prob_pred = 0
    for s in ['s1', 's2']: # s
        # Encuentro P(s' | s, a) en la tabla P
        trans_prob = 0
        for (next_s, prob) in P[s][a]:
            if next_s == s_prime:
                trans_prob = prob
                break
        prob_pred += trans_prob * b[s]
        
    # b'(s') (sin normalizar)
    b_new[s_prime] = prob_obs * prob_pred
    total_prob += b_new[s_prime]
    
# Normalizar (dividir por alfa, que es 'total_prob')
for s in b_new:
    b_new[s] = b_new[s] / total_prob
    
print(f"Creencia actualizada b'(s): {{'s1': {b_new['s1']:.2f}, 's2': {b_new['s2']:.2f}}}")
print("(Ahora creemos más que está lloviendo)")