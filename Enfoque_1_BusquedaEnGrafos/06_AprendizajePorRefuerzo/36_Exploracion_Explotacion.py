# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #36
# "Exploración vs. Explotación (Epsilon-Greedy)"

# Este es el *dilema* central del Refuerzo Activo.
#
# - Explotación: Usar el conocimiento actual para tomar
#   la mejor decisión. (Ej. Ir al restaurante que *sabes* que es bueno).
#
# - Exploración: Probar nuevas opciones (aleatorias) para
#   obtener nuevo conocimiento, arriesgándote a un mal resultado.
#   (Ej. Probar un restaurante nuevo que *podría* ser mejor).
#
# Epsilon-Greedy es la estrategia más simple para balancearlo.

import random
import time

# --- Ejemplo: Problema del "Bandido Multi-Brazo" ---
# 3 máquinas tragamonedas (brazos). Cada una da una recompensa aleatoria.
# El agente no sabe cuál es la mejor.

# Recompensas *reales* (El agente NO las ve)
# (Promedio, Desviación)
rewards_real = {
    'A': (5.0, 2.0), # Buena
    'B': (2.0, 1.0), # Mala
    'C': (4.5, 3.0)  # Ok, pero inconsistente
}

# Conocimiento del Agente (Q-values, promedio de recompensas vistas)
# Q(a)
Q = {'A': 0.0, 'B': 0.0, 'C': 0.0}
# Conteo de cuántas veces ha jugado cada una
N = {'A': 0, 'B': 0, 'C': 0}

# Función del simulador (el "casino")
def pull_arm(arm):
    mean, std_dev = rewards_real[arm]
    return random.normalvariate(mean, std_dev)

# --- Estrategia Epsilon-Greedy ---
def epsilon_greedy(epsilon):
    if random.random() < epsilon:
        # 1. Exploración
        print("  -> (Explorando)")
        return random.choice(list(Q.keys()))
    else:
        # 2. Explotación
        print("  -> (Explotando)")
        return max(Q, key=Q.get) # Devuelve el brazo con el Q-value más alto

# --- Simulación ---
NUM_JUEGOS = 50
epsilon = 0.3 # 30% de exploración

print(f"Estrategia Epsilon-Greedy (eps={epsilon})")
print(f"Q-values iniciales: {Q}")

for i in range(NUM_JUEGOS):
    
    # 1. Decidir qué brazo jugar
    arm = epsilon_greedy(epsilon)
    
    # 2. Jugar y observar recompensa
    reward = pull_arm(arm)
    
    # 3. Actualizar conocimiento (Q-value)
    # Q(a) = promedio de todas las recompensas de 'a'
    N[arm] += 1
    # Q_nuevo = Q_viejo + (1/N) * (Recompensa_nueva - Q_viejo)
    Q[arm] = Q[arm] + (1.0 / N[arm]) * (reward - Q[arm])
    
    if (i+1) % 10 == 0:
        print(f"\nJuego {i+1}")
        print(f"  Jugó: {arm}, Recompensa: {reward:.2f}")
        Q_rounded = {a: round(val, 2) for a, val in Q.items()}
        print(f"  Conteo N: {N}")
        print(f"  Q-values: {Q_rounded}")
        
print("\nSimulación terminada.")
print(f"Q-values finales (aprendidos): {Q_rounded}")
print(f"Recompensas reales (promedio): { {a: v[0] for a, v in rewards_real.items()} }")