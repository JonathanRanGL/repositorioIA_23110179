# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #13
# "Búsqueda de Temple Simulado (Simulated Annealing)"

import random
import math

# Temple Simulado: "Ascensión de Colinas que a veces acepta malos movimientos".
# Idea: Al principio ("alta temperatura"), es muy probable que acepte
# un movimiento "cuesta abajo" para explorar.
# Conforme pasa el tiempo ("se enfría"), se vuelve más exigente
# y solo acepta movimientos "cuesta arriba".

# Usaremos el mismo "paisaje"
landscape = [4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]
# Cima real en índice 11 (valor 15)
# Máximo local en índice 6 (valor 10)

def simulated_annealing(landscape, start_index, initial_temp, cooling_rate):
    
    current_index = start_index
    current_value = landscape[current_index]
    
    best_index_so_far = current_index
    best_value_so_far = current_value
    
    temp = initial_temp
    
    print(f"Iniciando en índice {current_index} (Valor: {current_value}), Temp: {temp:.2f}")

    while temp > 0.1: # Mientras no esté "congelado"
        
        # Elegir un vecino aleatorio (izquierda o derecha)
        move = random.choice([-1, 1])
        neighbor_index = current_index + move
        
        # Validar que el vecino esté en el mapa
        if not (0 <= neighbor_index < len(landscape)):
            continue # Si no es válido, intento otro movimiento
            
        neighbor_value = landscape[neighbor_index]
        
        # Calculo la "diferencia de energía"
        # Si es positivo, es un buen movimiento (cuesta arriba)
        # Si es negativo, es un mal movimiento (cuesta abajo)
        delta_value = neighbor_value - current_value
        
        # Decisión de aceptar el movimiento
        if delta_value > 0:
            # Siempre acepto un buen movimiento
            current_index = neighbor_index
            current_value = neighbor_value
            print(f"  Moviendo (Bien) a {current_index} (Valor: {current_value}), Temp: {temp:.2f}")
        else:
            # Acepto un mal movimiento basado en la probabilidad
            # Probabilidad = e^(delta / Temperatura)
            acceptance_prob = math.exp(delta_value / temp)
            if random.random() < acceptance_prob:
                current_index = neighbor_index
                current_value = neighbor_value
                print(f"  Moviendo (Mal) a {current_index} (Valor: {current_value}), Prob: {acceptance_prob:.2f}, Temp: {temp:.2f}")
                
        # Actualizo el mejor valor global si es necesario
        if current_value > best_value_so_far:
            best_value_so_far = current_value
            best_index_so_far = current_index
            print(f"    *** ¡Nuevo mejor valor encontrado: {best_value_so_far}! ***")

        # Enfriar la temperatura
        temp *= cooling_rate
            
    return best_index_so_far, best_value_so_far

# --- Ejemplo de uso ---
# Empezamos en el índice 6 (el máximo local de valor 10)
start_pos = 6
INITIAL_TEMP = 10.0   # Qué tan "caótico" es al inicio
COOLING_RATE = 0.95 # Qué tan rápido se enfría (ej. 0.95 = 5% por iteración)

print(f"Temple Simulado (Empezando en {start_pos}, Temp: {INITIAL_TEMP})")

peak_index, peak_value = simulated_annealing(landscape, start_pos, INITIAL_TEMP, COOLING_RATE)

print(f"\nResultado: Mejor valor encontrado en índice {peak_index} con valor {peak_value}")
print("(Logró 'bajar' del 10 para encontrar el 15 gracias a la aleatoriedad)")