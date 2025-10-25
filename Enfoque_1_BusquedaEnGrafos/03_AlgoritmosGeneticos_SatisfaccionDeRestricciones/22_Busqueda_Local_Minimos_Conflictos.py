# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #22
# "Búsqueda Local: Mínimos-Conflictos (Min-Conflicts)"

# Es un algoritmo de búsqueda *local* (como Hill Climbing).
# No construye la solución paso a paso, sino que:
# 1. Empieza con una asignación *completa* (pero mala, con errores).
# 2. En cada paso:
# 3. Elige una variable *en conflicto* (que viola una restricción).
# 4. Le asigna el valor que *minimice* el número de conflictos
#    con las otras variables.
# 5. Repite hasta que no haya conflictos.

# Problema clásico: N-Reinas
# Poner N reinas en un tablero NxN sin que se ataquen.

import random

# Función para contar conflictos de una reina específica
def count_conflicts(board, row, col, n):
    conflicts = 0
    for r in range(n):
        if r == row:
            continue
        c = board[r] # Columna de la reina en la fila 'r'
        
        # Conflicto horizontal (implícito, 1 reina por fila)
        # Conflicto vertical
        if c == col:
            conflicts += 1
        # Conflicto diagonal
        if abs(r - row) == abs(c - col):
            conflicts += 1
    return conflicts

# Función para encontrar el *total* de variables en conflicto
def find_conflicting_vars(board, n):
    conflicting = []
    for r in range(n):
        c = board[r]
        if count_conflicts(board, r, c, n) > 0:
            conflicting.append(r) # Guardo la fila (la variable)
    return conflicting

# Algoritmo Min-Conflicts
def min_conflicts(n, max_steps):
    
    # 1. Generar asignación inicial (aleatoria)
    # 'board' es un array donde board[fila] = columna
    board = [random.randint(0, n - 1) for _ in range(n)]
    
    print(f"Tablero inicial (N={n}): {board}")
    
    for i in range(max_steps):
        # 3. Encontrar variables en conflicto
        conflicting_vars = find_conflicting_vars(board, n)
        
        # Si no hay conflictos, ¡solución encontrada!
        if not conflicting_vars:
            print(f"\n¡Solución encontrada en {i} pasos!")
            return board
            
        # 3. Elegir una variable en conflicto aleatoriamente
        var_row = random.choice(conflicting_vars)
        
        # 4. Encontrar el valor (columna) que minimice conflictos
        min_conflicts_count = float('inf')
        best_col = board[var_row]
        
        for col in range(n): # Pruebo todas las columnas posibles
            count = count_conflicts(board, var_row, col, n)
            
            if count < min_conflicts_count:
                min_conflicts_count = count
                best_col = col
            # Si hay empate, nos quedamos con el primero (o aleatorio)
            
        # 4. Asignar el nuevo valor
        board[var_row] = best_col
        
        if i % 10 == 0: # Imprimo el progreso
             print(f"  Paso {i}, Conflictos: {len(conflicting_vars)}, Moviendo fila {var_row} a col {best_col}")

    print("\nSe alcanzó el máximo de pasos. No se encontró solución.")
    return board

# --- Ejemplo de uso ---
N = 8 # Problema de las 8 Reinas
MAX_STEPS = 1000

solution = min_conflicts(N, MAX_STEPS)
print(f"Tablero final: {solution}")