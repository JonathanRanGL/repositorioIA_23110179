# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #18
# "Búsqueda de Vuelta Atrás (Backtracking)"

# Es el algoritmo base para resolver CSPs.
# 1. Elige una variable sin asignar.
# 2. Elige un valor de su dominio.
# 3. Comprueba si el valor es "consistente" (no viola restricciones).
# 4. Si es consistente, sigue con la siguiente variable (recursión).
# 5. Si no es consistente, prueba otro valor.
# 6. Si se acaban los valores, "vuelve atrás" (backtrack) y cambia
#    la asignación de la variable *anterior*.

# Usamos la definición del CSP del archivo 17
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = {v: ['rojo', 'verde', 'azul'] for v in variables}
constraints = {
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'WA': ['NT'],
    'NT': ['Q'],
    'Q': ['NSW'],
    'NSW': ['V'],
    'V': [],
    'T': []
}
# (Formato de 'vecinos' para facilitar la comprobación)

# Función para comprobar consistencia
def is_consistent(variable, color, assignment, constraints):
    for neighbor in constraints.get(variable, []):
        # Si el vecino ya está asignado y tiene el mismo color...
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Función principal de backtracking
def backtracking_search(variables, domains, constraints, assignment={}):
    # Si todas las variables están asignadas, es una solución
    if len(assignment) == len(variables):
        return assignment
        
    # 1. Elige una variable sin asignar
    var = [v for v in variables if v not in assignment][0]
    
    # 2. Itera sobre los valores de su dominio
    for value in domains[var]:
        
        # 3. Comprueba si el valor es consistente
        if is_consistent(var, value, assignment, constraints):
            
            # 4. Asigna el valor
            assignment[var] = value
            # print(f"Probando {var} = {value}") # (Debug)
            
            # Llama recursivamente
            result = backtracking_search(variables, domains, constraints, assignment)
            
            # Si la recursión tuvo éxito, propaga el resultado
            if result is not None:
                return result
                
            # 5. Si la recursión falló, "vuelve atrás"
            # print(f"Fallo. Quitamos {var} = {value}") # (Debug)
            del assignment[var]
            
    # 6. Si se probaron todos los valores y ninguno funcionó
    return None

# --- Ejemplo de uso ---
print("Resolviendo CSP de colorear mapa con Backtracking...")
solution = backtracking_search(list(variables), domains, constraints)

if solution:
    print("\n¡Solución encontrada!")
    print(solution)
else:
    print("\nNo se encontró solución.")