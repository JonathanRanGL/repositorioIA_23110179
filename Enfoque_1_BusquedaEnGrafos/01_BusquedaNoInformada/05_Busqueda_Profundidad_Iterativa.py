# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #5
# "Búsqueda en Profundidad Iterativa (IDS)"

# Primero, necesitamos la Búsqueda en Profundidad Limitada (DLS)
def recursive_dls(node, goal, graph, path, limit, visited):
    if node == goal:
        return path
    if limit == 0:
        return "cutoff" # Indica que se alcanzó el límite
        
    visited.add(node)
    cutoff_occurred = False
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = recursive_dls(neighbor, goal, graph, path + [neighbor], limit - 1, visited.copy())
            
            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result
                
    return "cutoff" if cutoff_occurred else None

# Función DLS principal (wrapper)
def dls(start, goal, graph, limit):
    visited = set()
    return recursive_dls(start, goal, graph, [start], limit, visited)

# Ahora, la Búsqueda en Profundidad Iterativa (IDS)
def ids(start, goal, graph, max_depth):
    # Itero aumentando el límite de profundidad
    for limit in range(max_depth + 1):
        # Llamo a DLS con el límite actual
        result = dls(start, goal, graph, limit)
        
        # Si el resultado NO es 'cutoff'...
        if result != "cutoff":
            # ...o es el camino (éxito) o es None (fallo total)
            return result, limit
            
    # Si termino el bucle y solo obtuve "cutoff", no se encontró
    return None, max_depth

# --- Ejemplo de uso ---
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
# Un límite máximo razonable puede ser el número de nodos
max_limit = len(graph) 

print(f"Buscando camino de {start_node} a {goal_node} usando IDS...")
path, depth = ids(start_node, goal_node, graph, max_limit)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
    print(f"Encontrado en la profundidad: {depth}")
else:
    print("No se encontró un camino.")