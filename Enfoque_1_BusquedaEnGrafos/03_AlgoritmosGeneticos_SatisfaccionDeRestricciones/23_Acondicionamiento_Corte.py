# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #23
# "Acondicionamiento del Corte (Cutset Conditioning) - Concepto"

# Es un algoritmo para resolver CSPs.
# Idea: Muchos grafos de CSPs son "casi" un árbol. Los árboles
# son muy fáciles de resolver (tiempo lineal).
# El problema son los "ciclos" (ej. A->B->C->A).
#
# Acondicionamiento del Corte:
# 1. Identificar un "Cycle Cutset": un conjunto de variables
#    que, si se eliminan, "rompen" todos los ciclos y el
#    grafo restante se vuelve un árbol.
# 2. Para cada *asignación posible* de las variables del cutset:
# 3.   Asigna esos valores (ej. Cutset={'A'}, probar A='rojo')
# 4.   Propaga esas restricciones al resto del grafo (el "árbol").
# 5.   Resuelve el "árbol" restante (que es muy rápido).
# 6.   Si el árbol tiene solución, listo. Si no, prueba otra
#      asignación para el cutset (ej. A='verde').

# Este es un algoritmo conceptual.
# El siguiente código *simula* la lógica.

# --- Simulación ---
# Grafo del CSP:
# A -- B
# |    |
# C -- D
# (Un ciclo A-B-D-C-A)
#
# Variables = {A, B, C, D}
# Dominios = {rojo, verde}
# Restricciones = A!=B, B!=D, D!=C, C!=A

def solve_tree_csp(variables, domains, constraints):
    # En un CSP de árbol real, esto sería un algoritmo eficiente (O(n*d^2))
    # Aquí solo simulamos que tuvo éxito.
    print(f"    -> Resolviendo CSP (árbol) para {variables}...")
    # ... lógica de resolución de árbol ...
    print("    -> ¡Solución de árbol encontrada!")
    return {'B': 'verde', 'D': 'rojo', 'C': 'verde'} # Solución simulada

def cutset_conditioning():
    print("Simulación de Acondicionamiento del Corte")
    
    csp_variables = ['A', 'B', 'C', 'D']
    csp_domains = {v: ['rojo', 'verde'] for v in csp_variables}
    
    # 1. Identificar el Cutset.
    # Si quitamos 'A', el grafo queda: B - D - C (una línea, es un árbol).
    cutset_vars = ['A']
    tree_vars = ['B', 'C', 'D']
    
    print(f"Grafo original: {csp_variables}")
    print(f"Cutset identificado: {cutset_vars}")
    print(f"Árbol restante: {tree_vars}")
    
    # 2. Iterar sobre las asignaciones del cutset
    for value in csp_domains[cutset_vars[0]]:
        
        # 3. Asignar el valor
        cutset_assignment = {'A': value}
        print(f"\nProbando asignación del Cutset: {cutset_assignment}")
        
        # 4. Propagar restricciones (crear los dominios para el sub-problema)
        # (Aquí simulamos. En un caso real, eliminaríamos 'value'
        #  de los dominios de los vecinos de A, como B y C)
        print("  -> Propagando restricciones al árbol...")
        tree_domains = {'B': ['rojo', 'verde'], 'C': ['rojo', 'verde'], 'D': ['rojo', 'verde']}
        if value in tree_domains['B']: tree_domains['B'].remove(value)
        if value in tree_domains['C']: tree_domains['C'].remove(value)
        
        # 5. Resolver el CSP del árbol
        tree_solution = solve_tree_csp(tree_vars, tree_domains, {})
        
        if tree_solution:
            # 6. Solución encontrada
            final_solution = {**cutset_assignment, **tree_solution}
            print(f"\n¡Solución Global Encontrada!")
            print(final_solution)
            return final_solution
            
    print("\nNo se encontró solución global.")
    return None

# --- Ejemplo de uso ---
cutset_conditioning()