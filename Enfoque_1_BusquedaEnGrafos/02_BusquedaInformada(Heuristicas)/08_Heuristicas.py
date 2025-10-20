# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #8
# "Heurísticas"


# h(n): Estimación del costo desde el nodo 'n' hasta el 'objetivo'.

# Definimos un mapa de distancias en línea recta (heurística)
# desde cada nodo hasta el objetivo ('G')
heuristic_to_goal = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 4,
    'F': 2,
    'G': 0  # La heurística del objetivo a sí mismo siempre es 0
}

# --- Ejemplo de uso ---
# Cómo un algoritmo usaría esta heurística:

print("Ejemplo de Heurísticas (h(n))")
print("Estimación de costo (distancia en línea recta) hasta 'G':\n")

start_node = 'A'
goal_node = 'G'

# Supongamos que estamos en 'A' y podemos ir a 'B' o 'C'
# Grafo (solo para el ejemplo): {'A': ['B', 'C']}

# Decisión en 'A':
# ¿Ir a 'B' o 'C'?
# El algoritmo mira la heurística:
h_B = heuristic_to_goal['B']
h_C = heuristic_to_goal['C']

print(f"Heurística de 'B' a 'G' es: {h_B}")
print(f"Heurística de 'C' a 'G' es: {h_C}")

# Un algoritmo "voraz" (como el #9) elegiría 'C' porque h(C) es 7,
# que es menor que h(B) que es 8.
# "Parece" que 'C' está más cerca del objetivo.
if h_C < h_B:
    print("\nEl algoritmo elegiría 'C' porque 'parece' estar más cerca de 'G'.")
else:
    print("\nEl algoritmo elegiría 'B' porque 'parece' estar más cerca de 'G'.")