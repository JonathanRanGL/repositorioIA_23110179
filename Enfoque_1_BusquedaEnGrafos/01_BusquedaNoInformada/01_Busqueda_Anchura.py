# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #1
# "Búsqueda en Anchura (BFS)"

from collections import deque

def bfs(graph, start, goal):
    # La cola guarda (nodo, camino_hasta_ahora)
    queue = deque([(start, [start])])
    
    # Conjunto para no visitar nodos dos veces y evitar ciclos
    visited = set([start])
    
    while queue:
        # Saco el primer nodo de la cola (FIFO)
        (current_node, path) = queue.popleft()
        
        # Si es el objetivo, devuelvo el camino
        if current_node == goal:
            return path
            
        # Reviso los vecinos del nodo actual
        for neighbor in graph.get(current_node, []):
            # Si no lo he visitado...
            if neighbor not in visited:
                # ...lo marco como visitado
                visited.add(neighbor)
                
                # ...y lo añado a la cola con su nuevo camino
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                
    # Si la cola se vacía y no encontré el objetivo
    return None

# --- Ejemplo de uso ---
# Defino un grafo como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

start_node = 'A'
goal_node = 'G'

print(f"Buscando camino de {start_node} a {goal_node} usando BFS...")
path = bfs(graph, start_node, goal_node)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino.")