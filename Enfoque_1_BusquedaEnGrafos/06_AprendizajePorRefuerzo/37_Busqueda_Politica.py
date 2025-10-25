# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #37
# "Búsqueda de la Política (Policy Gradient - REINFORCE) - Concepto"

import numpy as np
import random 


theta = 0.0 # Inicial (P(A)=0.5, P(B)=0.5)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def get_policy(theta):
    prob_A = sigmoid(theta)
    return {'A': prob_A, 'B': 1.0 - prob_A}

def choose_action(policy):

    if random.random() < policy['A']:
        return 'A'
    return 'B'

def get_reward(action):
    return 1.0 if action == 'A' else 3.0

# --- Hiperparámetros ---
alfa = 0.1 # Tasa de aprendizaje (para theta)
NUM_EPISODIOS = 100

print("Búsqueda de Política (REINFORCE Conceptual)")
print(f"Recompensas: A=1, B=3")
print(f"Theta inicial: {theta:.2f}, Política inicial: {get_policy(theta)}")

for i in range(NUM_EPISODIOS):
    # 1. Ejecutar episodio (1 paso)
    policy = get_policy(theta)
    action = choose_action(policy)
    
    # 2. Obtener Recompensa Total (G)
    G = get_reward(action)
    
    # 3. Calcular el "Gradiente"
    # grad = d(log(pi(a|s))) / d(theta)
    # Para sigmoid(theta) -> P(A)
    # Si A fue elegido: grad = (1 - P(A))
    # Si B fue elegido: grad = -P(A)
    
    prob_A = policy['A']
    grad = 0.0
    if action == 'A':
        grad = (1 - prob_A)
    else: # B
        grad = -prob_A
        
    # 4. Actualizar theta
    # theta = theta + alfa * Gradiente * Recompensa
    # (Restamos una "línea base" (ej. 2.0) a G para estabilizar)
    baseline = 2.0 
    
    # Actualización de REINFORCE
    theta = theta + alfa * grad * (G - baseline)
    
    if (i+1) % 10 == 0:
        print(f"\nEpisodio {i+1}")
        print(f"  Acción: {action}, Recompensa G: {G}")
        print(f"  Grad: {grad:.2f}, (G-base): {G-baseline:.2f}")
        print(f"  Nuevo theta: {theta:.2f}, Nueva P(A): {get_policy(theta)['A']:.2f}")

print("\nEntrenamiento terminado.")
print(f"Theta final: {theta:.2f}")
print(f"Política final P(A)={get_policy(theta)['A']:.4f}, P(B)={get_policy(theta)['B']:.4f}")
print("(La política aprendió a preferir B, P(A) es muy bajo)")