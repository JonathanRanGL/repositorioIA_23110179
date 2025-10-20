# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #10
# "Búsqueda A* (A-Estrella)"

import heapq

# Búsqueda A*: "El equilibrio perfecto entre costo real y costo estimado".
# Usa f(n) = g(n) + h(n)
# g(n) = Costo real acumulado desde el inicio hasta 'n' (como UCS).
# h(n) = Costo estimado (heurística) desde 'n' hasta el objetivo (como Voraz).

def a_star(graph, start, goal, heuristic):
    # Cola de prioridad: (f_score, g_score, nodo, camino_hasta_ahora)
    # g_score se usa para comparar si encontramos un camino *mejor* a un nodo ya visto
    pqueue = [(heuristic[start], 0, start, [start])]
    
    # Nodos visitados y el *menor costo g(n)* para llegar a ellos
    visited = {}
    
    while pqueue:
        # Saco el nodo con el *menor f_score* (g + h)
        (f, g, current_node, path) = heapq.heappop(pqueue)
        
        # Si ya lo visité con un costo g *menor*, lo ignoro
        if current_node in visited and visited[current_node] < g:
            continue
            
        # Lo marco como visitado con su costo g
        visited[current_node] = g
        
        # Si es el objetivo, devuelvo el camino y el costo
        if current_node == goal:
            return path, g
            
        # Reviso los vecinos y sus costos
        for neighbor, weight in graph.get(current_node, []):
            
            # Calculo el nuevo costo g (costo real)
            new_g = g + weight
            
            # Si ya visité al vecino pero este camino es más caro, lo ignoro
            if neighbor in visited and visited[neighbor] < new_g:
                continue
                
            # Calculo el nuevo costo f (costo real + heurística)
            new_h = heuristic[neighbor]
            new_f = new_g + new_h
            
            new_path = path + [neighbor]
            
            # Añado el vecino a la cola de prioridad
            heapq.heappush(pqueue, (new_f, new_g, neighbor, new_path))
                
    # Si la cola se vacía y no encontré el objetivo
    return None, 0

# --- Ejemplo de uso ---
# Grafo con costos (el mismo de UCS)
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('D', 3), ('E', 7)],
    'C': [('A', 5), ('F', 4)],
    'D': [('B', 3)],
    'E': [('B', 7), ('F', 2)],
    'F': [('C', 4), ('E', 2), ('G', 1)],
    'G': [] # G es el final
}

# Heurística: Distancia estimada (en línea recta) hasta 'G'
# NOTA: Para que A* sea óptimo, la heurística debe ser "admisible"
# (nunca sobreestimar el costo real).
heuristic_to_goal = {
    'A': 8, 'B': 7, 'C': 4, 'D': 10,
    'E': 3, 'F': 1, 'G': 0,
}


start_node = 'A'
goal_node = 'G'

print(f"Buscando camino de {start_node} a {goal_node} usando A*...")
path, cost = a_star(graph, start_node, goal_node, heuristic_to_goal)

if path:
    # A* encuentra el camino óptimo (A->C->F->G)
    # UCS lo encontraría, pero A* lo hace explorando menos nodos
    print(f"Camino encontrado: {' -> '.join(path)}")
    print(f"Costo total: {cost}")
else:
    print("No se encontró un camino.")

# (Nota: AO* es un algoritmo diferente para grafos AND-OR,
# usados en descomposición de problemas, no en búsqueda de caminos simple).