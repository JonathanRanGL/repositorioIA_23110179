# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #27
# "Iteración de Valores (para un MDP)"

# La Iteración de Valores encuentra la utilidad óptima U(s) de cada estado
# en un Proceso de Decisión de Markov (MDP).
#
# Ecuación de Bellman:
# U(s) = R(s) + gamma * max_a [ SUMA( P(s'|s,a) * U(s') ) ]
#
# U(s) = Recompensa inmediata + (gamma * max_utilidad_futura_esperada)

# --- Ejemplo: Mundo de Celdas 1D ---
# Estados: 0, 1, 2, 3 (Meta)
# Recompensas: R(0)=-0.1, R(1)=-0.1, R(2)=-0.1, R(3)=+1
# Acciones: Izquierda, Derecha
# Transiciones: 80% éxito (va a donde quieres), 20% fallo (te quedas)
# Gamma: 0.9 (Factor de descuento)

# 1. Definir el MDP
states = [0, 1, 2, 3]
rewards = {0: -0.1, 1: -0.1, 2: -0.1, 3: 1}
gamma = 0.9

# U(s): Utilidad de los estados. Inicializo en 0.
U = {s: 0 for s in states}

# Función de Transición P(s' | s, a)
def transitions(s, a):
    if s == 3: # Estado terminal
        return [(3, 1.0)] # 100% se queda en 3
        
    s_prime_success = s
    if a == 'Der':
        s_prime_success = min(s + 1, 3) # Mover a la derecha (máx 3)
    elif a == 'Izq':
        s_prime_success = max(s - 1, 0) # Mover a la izquierda (mín 0)
        
    s_prime_fail = s # Falla = se queda
    
    # (s_siguiente, probabilidad)
    return [(s_prime_success, 0.8), (s_prime_fail, 0.2)]

# 2. Algoritmo de Iteración de Valores
K_iterations = 20
print(f"Iniciando Iteración de Valores (K={K_iterations}, gamma={gamma})")
print(f"U inicial: {U}")

for k in range(K_iterations):
    U_new = {} # Guardo las nuevas utilidades
    
    for s in states:
        if s == 3: # El estado terminal siempre tiene su propia recompensa
            U_new[s] = rewards[s]
            continue
            
        # Para este estado 's', calculo la utilidad de cada acción
        util_actions = {}
        for a in ['Izq', 'Der']:
            # SUMA( P(s'|s,a) * U(s') )
            expected_util = 0
            for s_prime, prob in transitions(s, a):
                expected_util += prob * U[s_prime] # Usa el U de la iteración k
            
            util_actions[a] = expected_util
            
        # max_a [...]
        max_future_util = max(util_actions.values())
        
        # Ecuación de Bellman
        U_new[s] = rewards[s] + (gamma * max_future_util)
        
    U = U_new # Actualizo U para la siguiente iteración k+1
    
    if k % 5 == 0 or k == K_iterations - 1:
        # Imprimo utilidades redondeadas
        U_rounded = {s: round(val, 2) for s, val in U.items()}
        print(f"Iter {k+1}: {U_rounded}")

print(f"\nUtilidad final (óptima) U(s):")
print(U)