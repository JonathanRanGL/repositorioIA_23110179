# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #2
# "Búsqueda en Anchura de Costo Uniforme (UCS)"

import heapq

def ucs(graph, start, goal):
    # Cola de prioridad: (costo_acumulado, nodo, camino_hasta_ahora)
    pqueue = [(0, start, [start])]
    
    # Conjunto para no visitar nodos dos veces (o con un costo mayor)
    visited = set()
    
    while pqueue:
        # Saco el nodo con el menor costo de la cola
        (cost, current_node, path) = heapq.heappop(pqueue)
        
        # Si ya lo visité con un costo menor, lo ignoro
        if current_node in visited:
            continue
            
        # Lo marco como visitado
        visited.add(current_node)
        
        # Si es el objetivo, devuelvo el camino y el costo
        if current_node == goal:
            return path, cost
            
        # Reviso los vecinos y sus costos
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                # Calculo el nuevo costo acumulado
                new_cost = cost + weight
                new_path = path + [neighbor]
                
                # Añado el vecino a la cola de prioridad
                heapq.heappush(pqueue, (new_cost, neighbor, new_path))
                
    # Si la cola se vacía y no encontré el objetivo
    return None, 0

# --- Ejemplo de uso ---
# Defino un grafo con pesos (costos)
# 'Nodo': [('Vecino1', costo1), ('Vecino2', costo2)]
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('D', 3), ('E', 7)],
    'C': [('A', 5), ('F', 4)],
    'D': [('B', 3)],
    'E': [('B', 7), ('F', 2)],
    'F': [('C', 4), ('E', 2), ('G', 1)],
    'G': ['F'] # G no tiene vecinos con costo (o es el final)
}

start_node = 'A'
goal_node = 'G'

print(f"Buscando camino de {start_node} a {goal_node} usando UCS...")
path, cost = ucs(graph, start_node, goal_node)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
    print(f"Costo total: {cost}")
else:
    print("No se encontró un camino.")