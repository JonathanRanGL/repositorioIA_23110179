# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #33
# "Aprendizaje por Refuerzo Pasivo (Temporal Difference)"

# Agente Pasivo: El agente tiene una política *fija* (pi) y
# no la cambia. Su objetivo es aprender la *Utilidad U(s)*
# de los estados bajo esa política.
#
# Aprende de "episodios" o "experiencias" (s, a, s', r).
#
# Actualización de Diferencia Temporal (Temporal Difference - TD):
# U(s) = U(s) + alfa * ( (R(s) + gamma * U(s')) - U(s) )
#
# U(s) se actualiza usando la "sorpresa":
# (Recompensa_inmediata + Utilidad_del_siguiente_estado) - (Lo_que_creía_que_valía_s)

import random

# --- Mismo MDP que en el Algoritmo 27 ---
# Estados: 0, 1, 2, 3 (Meta)
# Recompensas: R(0)=-0.1, R(1)=-0.1, R(2)=-0.1, R(3)=+1
# Gamma: 0.9 (Factor de descuento)
# Alfa: 0.1 (Tasa de aprendizaje)

rewards = {0: -0.1, 1: -0.1, 2: -0.1, 3: 1}
gamma = 0.9
alfa = 0.1 # Tasa de aprendizaje (qué tanto "confío" en la nueva info)

# U(s): Utilidad de los estados. Inicializo en 0.
U = {0: 0, 1: 0, 2: 0, 3: 0} # U(3) es 1, pero lo aprenderá

# 1. Política Fija (pi): Siempre ir a la derecha
pi = {0: 'Der', 1: 'Der', 2: 'Der', 3: 'Der'}

# Función de Transición (Simulador del mundo, el agente no lo ve)
def transitions(s, a):
    if s == 3: return 3
    
    if random.random() < 0.8: # 80% éxito
        s_prime = min(s + 1, 3) if a == 'Der' else max(s - 1, 0)
    else: # 20% fallo
        s_prime = s
    return s_prime

# --- Simulación de Aprendizaje ---
NUM_EPISODIOS = 500
print(f"Aprendizaje Pasivo (TD) (Política: siempre 'Der')")

for i in range(NUM_EPISODIOS):
    # Cada episodio empieza en el estado 0
    s = 0
    
    while s != 3: # Mientras no llegue a la meta
        
        # 1. Observar estado actual (s) y recompensa R(s)
        r = rewards[s]
        
        # 2. Ejecutar la acción de la política fija
        a = pi[s]
        
        # 3. Observar el siguiente estado (s')
        s_prime = transitions(s, a)
        
        # 4. Aplicar la Ecuación de Actualización TD
        # (Recompensa + Utilidad descontada del futuro)
        target_util = r + (gamma * U[s_prime]) 
        
        # (Lo que creía que valía este estado)
        current_util = U[s]
        
        # U(s) = U(s) + alfa * (target - current)
        U[s] = current_util + alfa * (target_util - current_util)
        
        # Avanzar al siguiente estado
        s = s_prime
        
    # La utilidad del estado meta (3) es su propia recompensa
    if U[3] == 0: U[3] = rewards[3]

    if (i+1) % 100 == 0:
        U_rounded = {st: round(val, 2) for st, val in U.items()}
        print(f"Episodio {i+1}: {U_rounded}")
        
print(f"\nUtilidad U(s) aprendida (TD Pasivo):")
print(U)