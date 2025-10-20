# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #9
# "Búsqueda Voraz Primero el Mejor (Greedy Best-First)"

import heapq

def greedy_best_first(graph, start, goal, heuristic):
    # Cola de prioridad: (valor_heurístico, nodo, camino_hasta_ahora)
    pqueue = [(heuristic[start], start, [start])]
    
    # Conjunto para no visitar nodos dos veces
    visited = set()
    
    while pqueue:
        # Saco el nodo con el *menor valor heurístico*
        (h, current_node, path) = heapq.heappop(pqueue)
        
        # Si ya lo visité, lo ignoro
        if current_node in visited:
            continue
            
        # Lo marco como visitado
        visited.add(current_node)
        
        # Si es el objetivo, devuelvo el camino
        if current_node == goal:
            return path
            
        # Reviso los vecinos
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # Calculo la heurística del vecino
                h_neighbor = heuristic[neighbor]
                new_path = path + [neighbor]
                
                # Añado el vecino a la cola de prioridad
                # La prioridad es solo la heurística h(n)
                heapq.heappush(pqueue, (h_neighbor, neighbor, new_path))
                
    # Si la cola se vacía y no encontré el objetivo
    return None

# --- Ejemplo de uso ---
# Grafo (solo conexiones, sin costo)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# Heurística: Distancia estimada (en línea recta) hasta 'G'
heuristic_to_goal = {
    'A': 10, 'B': 8, 'C': 7, 'D': 6,
    'E': 4, 'F': 2, 'G': 0,
}

start_node = 'A'
goal_node = 'G'

print(f"Buscando camino de {start_node} a {goal_node} usando Búsqueda Voraz...")
path = greedy_best_first(graph, start_node, goal_node, heuristic_to_goal)

if path:
    # Este camino (A->C->F->G) es el que la heurística guía
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino.")