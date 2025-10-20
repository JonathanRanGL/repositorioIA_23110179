# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #4
# "Búsqueda en Profundidad Limitada (DLS)"

# Esta es la función recursiva que hace el trabajo
def recursive_dls(node, goal, graph, path, limit, visited):
    # Si encontramos el objetivo
    if node == goal:
        return path
        
    # Si alcanzamos el límite de profundidad, paramos
    if limit == 0:
        return "cutoff" # Indica que se alcanzó el límite
        
    # Marco como visitado para esta rama
    visited.add(node)
    cutoff_occurred = False
    
    # Itero sobre los vecinos
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            # Llamada recursiva, resto 1 al límite
            result = recursive_dls(neighbor, goal, graph, path + [neighbor], limit - 1, visited.copy())
            
            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                # Si la llamada recursiva encontró el objetivo
                return result
                
    # Si exploré todo y no lo encontré en esta rama
    return "cutoff" if cutoff_occurred else None

# Función principal que inicializa DLS
def dls(start, goal, graph, limit):
    visited = set()
    return recursive_dls(start, goal, graph, [start], limit, visited)

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
depth_limit = 3

print(f"Buscando camino de {start_node} a {goal_node} con límite {depth_limit} (DLS)...")
path = dls(start_node, goal_node, graph, depth_limit)

if path == "cutoff":
    print(f"Se alcanzó el límite de profundidad {depth_limit} sin encontrar el objetivo.")
elif path:
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino dentro del límite.")

# Probamos con un límite mayor
depth_limit_2 = 4
print(f"\nBuscando camino de {start_node} a {goal_node} con límite {depth_limit_2} (DLS)...")
path_2 = dls(start_node, goal_node, graph, depth_limit_2)

if path_2 == "cutoff":
    print(f"Se alcanzó el límite de profundidad {depth_limit_2} sin encontrar el objetivo.")
elif path_2:
    print(f"Camino encontrado: {' -> '.join(path_2)}")
else:
    print("No se encontró un camino dentro del límite.")