# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #11
# "Búsqueda de Ascensión de Colinas (Hill Climbing)"

import random

# Ascensión de Colinas: "Toma el camino que te lleve cuesta arriba".
# Es una búsqueda local simple. Solo mira a sus vecinos inmediatos
# y se mueve al mejor de ellos. No "recuerda" el pasado.
# Problema: Se atora en "máximos locales" (colinas pequeñas).

# Definimos el "paisaje" o "problema"
# Queremos encontrar el valor más alto (la cima de la colina)
# Esto es solo una lista de números para el ejemplo
landscape = [4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]

def hill_climbing(landscape, start_index):
    current_index = start_index
    current_value = landscape[current_index]
    
    print(f"Iniciando en índice {current_index} (Valor: {current_value})")
    
    while True:
        best_neighbor_index = -1
        best_neighbor_value = -float('inf') # Infinito negativo
        
        # Miro a mis vecinos (izquierda y derecha)
        for move in [-1, 1]:
            neighbor_index = current_index + move
            
            # Reviso que el vecino esté dentro del mapa
            if 0 <= neighbor_index < len(landscape):
                neighbor_value = landscape[neighbor_index]
                
                # Si este vecino es mejor que el mejor que he visto
                if neighbor_value > best_neighbor_value:
                    best_neighbor_value = neighbor_value
                    best_neighbor_index = neighbor_index
                    
        # Comparo el mejor vecino con mi posición actual
        if best_neighbor_value > current_value:
            # Me muevo al mejor vecino
            print(f"  Moviendo a índice {best_neighbor_index} (Valor: {best_neighbor_value})")
            current_index = best_neighbor_index
            current_value = best_neighbor_value
        else:
            # Si no hay vecinos mejores, he llegado a una cima
            print(f"  No hay vecinos mejores. Cima local encontrada.")
            break
            
    return current_index, current_value

# --- Ejemplo de uso ---
# Empezamos en un punto aleatorio
start_pos = random.randint(0, len(landscape) - 1)

peak_index, peak_value = hill_climbing(landscape, start_pos)

print(f"\nResultado: Cima encontrada en índice {peak_index} con valor {peak_value}")

# Nota: Si empieza en el índice 6 (valor 10), se atorará ahí
# y no encontrará la verdadera cima global (índice 11, valor 15).
print("\n--- Nueva Búsqueda ---")
start_pos_2 = 6
peak_index_2, peak_value_2 = hill_climbing(landscape, start_pos_2)
print(f"Resultado: Cima encontrada en índice {peak_index_2} con valor {peak_value_2}")
print("(Se atoró en un máximo local, no encontró el 15)")