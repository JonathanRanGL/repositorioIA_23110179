# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #16
# "Búsqueda Online (LRTA*)"

# Búsqueda Online: "Tomar decisiones sin conocer el mapa completo".
# El agente solo ve sus vecinos inmediatos. Se mueve, y *luego*
# actualiza su "estimación" (heurística) del costo del lugar donde *estaba*.
# LRTA* (Learning Real-Time A*) es un ejemplo.

# f(n) = g(n) + h(n)
# g(n) = costo real del movimiento (siempre 1 en este ejemplo)
# h(n) = heurística (estimación aprendida)

# --- Definición del Problema (El Agente NO lo ve) ---
# Un laberinto simple de 1D: [0, 1, 2, 3(Meta)]
# Costo de moverse (g(n)) es 1.
goal_pos = 3
# El mapa real de costos (el agente no lo sabe)
# Costos reales: 3, 2, 1, 0
real_costs = {0: 3, 1: 2, 2: 1, 3: 0}


# --- Lo que el Agente sabe ---
# El agente solo sabe su posición actual y su tabla de heurísticas,
# que al inicio es una mala estimación (ej. todos son 0).
# h(n)
heuristic_table = {0: 0, 1: 0, 2: 0, 3: 0}
current_pos = 0

print(f"Búsqueda Online (LRTA*) - Meta en {goal_pos}")
print(f"Estado inicial: Pos={current_pos}, H = {heuristic_table}")

MAX_STEPS = 10
for i in range(MAX_STEPS):
    
    # 1. Comprobar si ya llegué
    if current_pos == goal_pos:
        print(f"\n¡Meta encontrada en el paso {i}!")
        break
        
    # 2. Mirar a los vecinos y calcular f(n) = g(n) + h(n)
    # g(n) es 1 (costo de 1 paso)
    # h(n) es la heurística del vecino
    
    best_move = -1
    min_f_score = float('inf')
    
    print(f"\n--- Paso {i+1} (Posición actual: {current_pos}) ---")
    
    for move in [-1, 1]:
        neighbor_pos = current_pos + move
        
        # Validar vecino
        if neighbor_pos in real_costs:
            h_neighbor = heuristic_table[neighbor_pos]
            g_move = 1
            f_score = g_move + h_neighbor
            
            print(f"  Vecino {neighbor_pos}: f = g(1) + h({h_neighbor}) = {f_score}")
            
            if f_score < min_f_score:
                min_f_score = f_score
                best_move = neighbor_pos
                
    # 3. Actualizar la heurística del nodo *actual* (donde estaba)
    # "El costo de donde estoy (h[s]) será el costo del mejor vecino (f[s'])"
    print(f"  Actualizando H[{current_pos}]: Nuevo valor = {min_f_score}")
    heuristic_table[current_pos] = min_f_score
    
    # 4. Moverse al mejor vecino
    print(f"  Moviendo a: {best_move}")
    current_pos = best_move
    
    print(f"  Tabla H actualizada: {heuristic_table}")

print(f"\nTabla Heurística Final (Aprendida): {heuristic_table}")
print(f"Tabla Heurística Real:            {real_costs}")