# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #6
# "Búsqueda Bidireccional"

from collections import deque

def bidirectional_search(graph, start, goal):
    # Cola para la búsqueda desde el inicio (BFS)
    q_start = deque([(start, [start])])
    # Cola para la búsqueda desde el objetivo (BFS)
    q_goal = deque([(goal, [goal])])
    
    # Nodos visitados desde el inicio (guarda el camino)
    visited_start = {start: [start]}
    # Nodos visitados desde el objetivo (guarda el camino)
    visited_goal = {goal: [goal]}
    
    while q_start and q_goal:
        
        # --- Expansión desde el INICIO ---
        if q_start:
            current_s, path_s = q_start.popleft()
            
            # Si el nodo de inicio se topa con la búsqueda del objetivo...
            if current_s in visited_goal:
                # ...unimos los caminos (invirtiendo el de 'goal')
                return path_s + visited_goal[current_s][::-1][1:] # [1:] para no duplicar el nodo
            
            for neighbor in graph.get(current_s, []):
                if neighbor not in visited_start:
                    new_path_s = path_s + [neighbor]
                    visited_start[neighbor] = new_path_s
                    q_start.append((neighbor, new_path_s))

        # --- Expansión desde el OBJETIVO ---
        if q_goal:
            current_g, path_g = q_goal.popleft()
            
            # Si el nodo de objetivo se topa con la búsqueda de inicio...
            if current_g in visited_start:
                # ...unimos los caminos (invirtiendo el de 'goal')
                return visited_start[current_g] + path_g[::-1][1:] # [1:] para no duplicar el nodo
                
            for neighbor in graph.get(current_g, []):
                if neighbor not in visited_goal:
                    new_path_g = path_g + [neighbor]
                    visited_goal[neighbor] = new_path_g
                    q_goal.append((neighbor, new_path_g))
                    
    # Si una cola se vacía, no hay conexión
    return None

# --- Ejemplo de uso ---
# Usamos un grafo no dirigido (o donde las conexiones son simétricas)
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

print(f"Buscando camino de {start_node} a {goal_node} usando Búsqueda Bidireccional...")
path = bidirectional_search(graph, start_node, goal_node)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino.")