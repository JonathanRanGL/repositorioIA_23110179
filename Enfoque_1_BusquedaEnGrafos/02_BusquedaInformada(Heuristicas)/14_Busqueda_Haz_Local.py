# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #14
# "Búsqueda de Haz Local (Local Beam Search)"

import random

# Búsqueda de Haz Local: "K ascensiones de colinas que se comunican".
# En lugar de 1 explorador (Hill Climbing), empezamos con K exploradores
# en puntos aleatorios del mapa.
# En cada paso:
# 1. Todos los K exploradores miran a sus vecinos.
# 2. Se genera una lista de *todos* los vecinos de *todos* los exploradores.
# 3. Se eligen los K mejores vecinos de esa lista global.
# 4. Esos K mejores vecinos se convierten en los *nuevos* exploradores.

# Usaremos el mismo "paisaje"
landscape = [4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]
# Cima real en índice 11 (valor 15)

def local_beam_search(landscape, k, max_iterations):
    
    # 1. Empezar con K exploradores (estados) aleatorios
    current_states_indices = random.sample(range(len(landscape)), k)
    current_states = [(idx, landscape[idx]) for idx in current_states_indices]
    
    print(f"Iniciando con K={k} exploradores en: {current_states}")
    
    best_index_so_far = -1
    best_value_so_far = -float('inf')
    
    # Actualizo el mejor valor inicial
    for idx, val in current_states:
        if val > best_value_so_far:
            best_value_so_far = val
            best_index_so_far = idx

    for i in range(max_iterations):
        all_neighbors = []
        
        # 2. Todos los K exploradores generan a sus vecinos
        for current_idx, current_val in current_states:
            for move in [-1, 1]:
                neighbor_idx = current_idx + move
                
                # Si el vecino es válido
                if 0 <= neighbor_idx < len(landscape):
                    neighbor_val = landscape[neighbor_idx]
                    # Guardo (índice, valor)
                    all_neighbors.append((neighbor_idx, neighbor_val))

        # Si no hay vecinos (raro), paro
        if not all_neighbors:
            print("  No se generaron más vecinos.")
            break
            
        # 3. Ordeno la lista global de vecinos de mejor a peor
        all_neighbors.sort(key=lambda x: x[1], reverse=True)
        
        # 4. Elijo los K mejores vecinos como los nuevos exploradores
        # Usamos un set para evitar duplicados en los nuevos estados
        new_states_set = set()
        for idx, val in all_neighbors:
            if len(new_states_set) < k:
                new_states_set.add((idx, val))
            else:
                break
        
        current_states = list(new_states_set)
        
        # Actualizo el mejor valor global
        best_of_this_round = current_states[0] # Ya están ordenados (o casi)
        if best_of_this_round[1] > best_value_so_far:
            best_value_so_far = best_of_this_round[1]
            best_index_so_far = best_of_this_round[0]
            print(f"  Iter {i}: ¡Nuevo mejor valor {best_value_so_far}!")
        else:
            print(f"  Iter {i}: Exploradores en {current_states}")
            
        # Si todos los exploradores llegan a la misma cima, paro
        if len(current_states) == 0:
            print("  Exploradores agotados.")
            break

    return best_index_so_far, best_value_so_far

# --- Ejemplo de uso ---
K = 3 # Número de "exploradores"
MAX_ITERATIONS = 5

print(f"Búsqueda de Haz Local (K={K})")
peak_index, peak_value = local_beam_search(landscape, K, MAX_ITERATIONS)

print(f"\nResultado: Mejor valor encontrado en índice {peak_index} con valor {peak_value}")