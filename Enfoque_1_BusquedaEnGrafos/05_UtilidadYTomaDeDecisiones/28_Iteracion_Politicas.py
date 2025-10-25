# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #28
# "Iteración de Políticas (para un MDP)"

# La Iteración de Políticas encuentra la política óptima pi(s)
# (qué acción tomar en cada estado).
#
# Alterna dos pasos:
# 1. Evaluación de Política: Dado pi, calcular U(s).
#    (Similar a Iter. de Valores, pero *sin* el 'max_a')
# 2. Mejora de Política: Dado U(s), encontrar la *mejor*
#    acción 'a' para cada estado, creando una nueva pi.
#
# Repetir hasta que la política no cambie.

import copy

# --- Mismo MDP que en el Algoritmo 27 ---
states = [0, 1, 2, 3]
rewards = {0: -0.1, 1: -0.1, 2: -0.1, 3: 1}
gamma = 0.9

# Función de Transición P(s' | s, a)
def transitions(s, a):
    if s == 3: return [(3, 1.0)]
    s_prime_success = min(s + 1, 3) if a == 'Der' else max(s - 1, 0)
    s_prime_fail = s
    return [(s_prime_success, 0.8), (s_prime_fail, 0.2)]

# --- Algoritmo de Iteración de Políticas ---

# 1. Política Inicial (aleatoria, ej. siempre 'Der')
pi = {0: 'Der', 1: 'Der', 2: 'Der', 3: 'Der'} # pi(s) = a
U = {s: 0 for s in states}

MAX_POLICY_ITERATIONS = 10
K_EVALUATION_STEPS = 10 # Pasos para evaluar U(s)

print(f"Iniciando Iteración de Políticas (gamma={gamma})")

for i in range(MAX_POLICY_ITERATIONS):
    print(f"\n--- Iteración de Política {i+1} ---")
    print(f"Política actual pi(s): {pi}")
    
    # --- 1. Evaluación de Política (Calcular U(s) para pi) ---
    # U_pi(s) = R(s) + gamma * SUMA( P(s'|s, pi(s)) * U_pi(s') )
    
    U_pi = {s: 0 for s in states} # Reseteo utilidades
    
    for k in range(K_EVALUATION_STEPS):
        U_pi_new = {}
        for s in states:
            if s == 3:
                U_pi_new[s] = rewards[s]
                continue
                
            a = pi[s] # Acción fija de la política
            expected_util = 0
            for s_prime, prob in transitions(s, a):
                expected_util += prob * U_pi[s_prime]
            
            U_pi_new[s] = rewards[s] + (gamma * expected_util)
        U_pi = U_pi_new
        
    print(f"Utilidad evaluada U(s): {{ {', '.join(f'{k}: {v:.2f}' for k, v in U_pi.items())} }}")

    # --- 2. Mejora de Política (Calcular nueva pi(s) usando U(s)) ---
    # pi_new(s) = argmax_a [ SUMA( P(s'|s, a) * U(s') ) ]
    
    pi_new = {}
    policy_changed = False
    
    for s in states:
        if s == 3:
            pi_new[s] = 'Der' # No importa
            continue
            
        util_actions = {}
        for a in ['Izq', 'Der']:
            expected_util = 0
            for s_prime, prob in transitions(s, a):
                expected_util += prob * U_pi[s_prime]
            util_actions[a] = expected_util
            
        # Encontrar la mejor acción
        best_a = max(util_actions, key=util_actions.get)
        pi_new[s] = best_a
        
        # Comprobar si la política cambió
        if pi_new[s] != pi[s]:
            policy_changed = True
            
    # 3. Comprobar convergencia
    if not policy_changed:
        print("\nLa política convergió. Terminando.")
        break
    
    pi = pi_new # Actualizar la política para la siguiente iteración

print(f"\nPolítica Óptima pi(s): {pi}")
print(f"Utilidad Óptima U(s):")
print(U_pi)