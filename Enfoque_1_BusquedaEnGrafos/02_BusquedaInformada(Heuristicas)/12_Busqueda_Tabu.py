# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #12
# "Búsqueda Tabú"

import random

# Búsqueda Tabú: "Ascensión de Colinas con memoria".
# Para evitar atorarse en máximos locales, mantiene una "lista tabú"
# de los últimos movimientos realizados.
# Si un movimiento está en la lista tabú, no lo repite,
# forzándolo a explorar otras zonas.

# Usaremos el mismo "paisaje" que en Ascensión de Colinas
landscape = [4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]
# La cima real está en el índice 11 (valor 15)
# Un máximo local está en el índice 6 (valor 10)

def tabu_search(landscape, start_index, tabu_size, max_iterations):
    
    current_index = start_index
    current_value = landscape[current_index]
    
    best_index_so_far = current_index
    best_value_so_far = current_value
    
    # La "memoria" o lista tabú (guarda los *índices* visitados)
    tabu_list = []
    
    print(f"Iniciando en índice {current_index} (Valor: {current_value})")
    
    for _ in range(max_iterations):
        best_neighbor_index = -1
        best_neighbor_value = -float('inf')
        
        # Miro a mis vecinos (izquierda y derecha)
        for move in [-1, 1]:
            neighbor_index = current_index + move
            
            # Reviso que esté en el mapa Y que NO esté en la lista tabú
            if 0 <= neighbor_index < len(landscape) and neighbor_index not in tabu_list:
                neighbor_value = landscape[neighbor_index]
                
                # Busco el mejor vecino *no tabú*
                if neighbor_value > best_neighbor_value:
                    best_neighbor_value = neighbor_value
                    best_neighbor_index = neighbor_index
        
        # Si no encontré vecinos (ambos son tabú o estoy en un borde)
        if best_neighbor_index == -1:
            print("  No hay vecinos válidos no-tabú. Parando.")
            break
            
        # Me muevo al mejor vecino (incluso si es peor que mi posición actual)
        current_index = best_neighbor_index
        current_value = best_neighbor_value
        print(f"  Moviendo a índice {current_index} (Valor: {current_value})")

        # Añado el *nuevo* índice a la lista tabú
        tabu_list.append(current_index)
        
        # Si la lista tabú es muy grande, quito el más antiguo
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
            
        # Actualizo mi "mejor solución" global
        if current_value > best_value_so_far:
            best_value_so_far = current_value
            best_index_so_far = current_index
            print(f"  *** ¡Nuevo mejor valor encontrado: {best_value_so_far}! ***")
            
    return best_index_so_far, best_value_so_far

# --- Ejemplo de uso ---
# Empezamos en el índice 6 (el máximo local de valor 10)
start_pos = 6
TABU_SIZE = 2      # Memoria corta: "No visitar los 2 últimos lugares"
MAX_ITERATIONS = 10 # Cuántos pasos daremos

print(f"Búsqueda Tabú (Empezando en {start_pos}, Tamaño Tabú: {TABU_SIZE})")

peak_index, peak_value = tabu_search(landscape, start_pos, TABU_SIZE, MAX_ITERATIONS)

print(f"\nResultado: Mejor valor encontrado en índice {peak_index} con valor {peak_value}")
print("(Logró 'bajar' del 10 para encontrar el 15)")