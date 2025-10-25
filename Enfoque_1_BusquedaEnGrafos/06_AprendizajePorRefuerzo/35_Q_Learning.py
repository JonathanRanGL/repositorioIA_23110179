# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #35
# "Q-Learning"

# Q-Learning es un algoritmo de Refuerzo Activo *Model-Free*.
# "Model-Free" = No intenta aprender P(s'|s,a) o R(s).
#
# Aprende la "Q-Function" (Función de Calidad) Q(s, a),
# que representa la utilidad esperada de tomar la acción 'a'
# en el estado 's' y seguir la política óptima después.
#
# Ecuación de Actualización de Q-Learning (es una forma de TD):
# Q(s,a) = Q(s,a) + alfa * ( [R(s) + gamma * max_a' Q(s',a')] - Q(s,a) )
#
# "Lo_que_creía" = Q(s,a)
# "Lo_que_aprendí" = R(s) + gamma * (El Q-value más alto del *siguiente* estado)

import random

# --- Mismo MDP que en el Algoritmo 27 ---
states = [0, 1, 2, 3]
actions = ['Izq', 'Der']
rewards = {0: -0.1, 1: -0.1, 2: -0.1, 3: 1} # R(s)
gamma = 0.9
alfa = 0.1

# Q-Table: Q(s, a). Inicializo todo en 0.
Q = {s: {a: 0.0 for a in actions} for s in states}
# (La Q-Table del estado meta (3) es siempre 0, ya que no hay acciones futuras)

# Función de Transición (Simulador del mundo)
def transitions(s, a):
    if s == 3: return 3
    if random.random() < 0.8: # 80% éxito
        s_prime = min(s + 1, 3) if a == 'Der' else max(s - 1, 0)
    else: # 20% fallo
        s_prime = s
    return s_prime

# Política Epsilon-Greedy (Ver Algoritmo 36)
def choose_action(s, epsilon):
    if random.random() < epsilon:
        # Exploración
        return random.choice(actions)
    else:
        # Explotación (elegir la mejor acción 'a' basada en Q(s,a))
        return max(Q[s], key=Q[s].get)

# --- Simulación de Q-Learning ---
NUM_EPISODIOS = 1000
epsilon = 0.1 # 10% de exploración

print(f"Iniciando Q-Learning (alfa={alfa}, gamma={gamma}, eps={epsilon})")

for i in range(NUM_EPISODIOS):
    s = 0 # Empezar en estado 0
    
    while s != 3: # Mientras no llegue a la meta
        
        # 1. Elegir acción (a) usando la política (Epsilon-Greedy)
        a = choose_action(s, epsilon)
        
        # 2. Ejecutar (a) y observar s' y r
        s_prime = transitions(s, a)
        r = rewards[s_prime] # Recompensa se recibe al *llegar* a s_prime
        if s == 2 and s_prime == 3: # Corrección: uso la recompensa de *este* estado
             r = rewards[s] # (En este MDP R(s) se da al estar en s)
        
        # 3. Aplicar Ecuación de Q-Learning
        
        # Lo_que_creía
        q_current = Q[s][a]
        
        # max_a' Q(s', a')
        # (El mejor Q-value que puedo obtener desde el *siguiente* estado)
        q_max_future = 0
        if s_prime != 3:
             q_max_future = max(Q[s_prime].values())
        else:
             q_max_future = rewards[s_prime] # Utilidad del estado meta es su recompensa
             
        # "Lo_que_aprendí" (Target)
        q_target = rewards[s] + (gamma * q_max_future) # Usamos R(s)
        
        # Actualización
        Q[s][a] = q_current + alfa * (q_target - q_current)
        
        # Avanzar
        s = s_prime

print("\nQ-Table final aprendida (Q(s, a)):")
for s in states:
    Q_rounded = {a: round(val, 2) for a, val in Q[s].items()}
    print(f"  Estado {s}: {Q_rounded}")

# Derivar la Política Óptima pi(s) desde la Q-Table
pi_optima = {}
for s in states:
    if s != 3:
        pi_optima[s] = max(Q[s], key=Q[s].get)
print(f"\nPolítica Óptima derivada: {pi_optima}")