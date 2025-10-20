# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #3
# "Búsqueda en Profundidad (DFS)"

def dfs(graph, start, goal):
    # La pila (stack) guarda (nodo, camino_hasta_ahora)
    stack = [(start, [start])]
    
    # Conjunto para no visitar nodos dos veces
    visited = set()
    
    while stack:
        # Saco el último nodo de la pila (LIFO)
        (current_node, path) = stack.pop()
        
        # Si no lo he visitado...
        if current_node not in visited:
            
            # Si es el objetivo, devuelvo el camino
            if current_node == goal:
                return path
                
            # Lo marco como visitado
            visited.add(current_node)
            
            # Reviso los vecinos (en orden inverso para que la pila los procese en orden)
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    # Añado el vecino a la pila
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
                    
    # Si la pila se vacía y no encontré el objetivo
    return None

# --- Ejemplo de uso ---
# Defino un grafo como un diccionario
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

print(f"Buscando camino de {start_node} a {goal_node} usando DFS...")
path = dfs(graph, start_node, goal_node)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino.")