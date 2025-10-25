# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #19
# "Comprobación Hacia Delante (Forward Checking)"

# Es una mejora de Backtracking.
# Cuando asignamos un valor (ej. 'WA' = 'rojo'), Backtracking no hace nada.
# Forward Checking "mira hacia adelante":
# 1. Asigna 'WA' = 'rojo'.
# 2. Inmediatamente, va a los dominios de *todos sus vecinos* (NT, SA)
#    y *elimina* 'rojo' de sus dominios.
# 3. Si algún vecino se queda con el dominio vacío, la asignación
#    'WA' = 'rojo' es inválida y se descarta *inmediatamente*.

import copy

# Definición del CSP (igual que en Backtracking)
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
initial_domains = {v: ['rojo', 'verde', 'azul'] for v in variables}
constraints = {
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'WA': ['NT', 'SA'], # Agregado SA
    'NT': ['WA', 'SA', 'Q'], # Agregados vecinos
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['NSW', 'SA'],
    'T': []
}

# Función principal
def forward_checking_search(variables, domains, constraints, assignment={}):
    if len(assignment) == len(variables):
        return assignment
        
    var = [v for v in variables if v not in assignment][0]
    
    for value in list(domains[var]): # Itero sobre una copia
        
        # 1. Asignación provisional
        assignment[var] = value
        # print(f"Probando {var} = {value}")
        
        # 2. Hago "Forward Checking": reduzco dominios de vecinos
        # Guardo los dominios originales por si tengo que hacer backtrack
        domains_copy = copy.deepcopy(domains) 
        
        # Esta es la parte clave de Forward Checking
        consistent = True
        for neighbor in constraints[var]:
            if neighbor not in assignment:
                # Si el valor está en el dominio del vecino...
                if value in domains_copy[neighbor]:
                    # ...lo elimino
                    domains_copy[neighbor].remove(value)
                    
                # 3. Si un vecino se queda sin dominio, es un fallo
                if not domains_copy[neighbor]:
                    consistent = False
                    # print(f"  Fallo: {neighbor} se quedó sin dominio.")
                    break # Salgo del bucle de vecinos
        
        # Si la asignación fue consistente (ningún vecino quedó vacío)
        if consistent:
            result = forward_checking_search(variables, domains_copy, constraints, assignment)
            if result is not None:
                return result
                
        # Backtrack: quito la asignación
        del assignment[var]
        # (No necesito restaurar 'domains', porque la siguiente iteración
        #  del bucle 'for value...' usará la 'domains_copy' de esa llamada)
        
    return None

# --- Ejemplo de uso ---
print("Resolviendo CSP con Backtracking + Forward Checking...")
# Hacemos una copia profunda porque la función modifica los dominios
solution = forward_checking_search(variables, copy.deepcopy(initial_domains), constraints)

if solution:
    print("\n¡Solución encontrada!")
    print(solution)
else:
    print("\nNo se encontró solución.")