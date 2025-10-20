# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #7
# "Búsqueda en Grafos (Concepto)"

from collections import deque

# Este es un ejemplo de 'Búsqueda en Grafos' genérica.
# La clave de una "Búsqueda en Grafos" (a diferencia de "Búsqueda en Árboles")...
# ...es el uso de un conjunto 'visited' (o 'explorados') para evitar ciclos
# y no procesar el mismo nodo múltiples veces.

# Usaremos una cola (BFS) como estrategia de exploración para demostrarlo.
def generic_graph_search(graph, start, goal):
    
    # Cola para nodos por explorar
    queue = deque([start])
    
    # El conjunto 'visited' es lo que define la búsqueda en *grafos*
    visited = {start}
    
    # Opcional: para rastrear el camino
    parent = {start: None}
    
    print("Iniciando Búsqueda en Grafo...")
    print(f"Visitados: {visited}")
    print(f"Cola: {list(queue)}")

    while queue:
        # Mientras haya nodos por explorar
        node = queue.popleft()
        print(f"\nProcesando nodo: {node}")
        
        # Si es el objetivo, terminamos
        if node == goal:
            print(f"¡Objetivo {goal} encontrado!")
            # Reconstruimos el camino
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1] # Devolvemos el camino en orden
            
        # Reviso sus vecinos
        for neighbor in graph.get(node, []):
            # Si no lo he visitado *nunca*...
            if neighbor not in visited:
                # ...lo marco como visitado
                visited.add(neighbor)
                # ...guardo quién es su padre
                parent[neighbor] = node
                # ...y lo añado a la cola
                queue.append(neighbor)
                
                print(f"  -> Vecino {neighbor} no visitado. Añadido a visitados y a la cola.")
                print(f"     Visitados: {visited}")
                print(f"     Cola: {list(queue)}")
            else:
                print(f"  -> Vecino {neighbor} ya está en 'visitados'. Ignorando.")

    print(f"Cola vacía. No se encontró el objetivo {goal}.")
    return None

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

path = generic_graph_search(graph, start_node, goal_node)

if path:
    print(f"\nCamino final: {' -> '.join(path)}")
else:
    print("\nNo se encontró un camino.")