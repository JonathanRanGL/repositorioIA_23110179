# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #20
# "Propagación de Restricciones (Arc Consistency - AC-3)"

# AC-3 es un *pre-procesamiento*. No resuelve el CSP, pero
# "limpia" los dominios *antes* de empezar el Backtracking.
#
# Idea: Un arco (V1, V2) es consistente si *para cada valor*
# en el dominio de V1, existe *algún valor* en el dominio de V2
# que no viola la restricción.
#
# Si 'WA' tiene ['rojo'] y su vecino 'NT' tiene ['rojo'],
# el arco (WA, NT) no es consistente, porque si WA = 'rojo',
# NT no tiene ningún valor válido.
# AC-3 eliminaría 'rojo' de WA (dejándolo vacío).

# Definición del CSP
variables = ['WA', 'NT', 'Q']
domains = {
    'WA': ['rojo', 'verde'],
    'NT': ['rojo'], # Dominio problemático
    'Q': ['rojo', 'verde']
}
# Restricciones (solo arcos)
constraints = [('WA', 'NT'), ('NT', 'WA'), ('NT', 'Q'), ('Q', 'NT')]

# Función que revisa si un arco (v1, v2) es consistente
# y elimina valores de v1 si es necesario.
def revise(v1, v2, domains):
    revised = False
    # Para cada valor 'x' en el dominio de v1...
    for x in list(domains[v1]): # Copia para poder modificar
        # ...busco si existe un valor 'y' en v2 que sea compatible
        compatible = False
        for y in domains[v2]:
            if x != y: # La restricción es "no ser iguales"
                compatible = True
                break
        
        # Si no encontré ningún 'y' compatible...
        if not compatible:
            # ...elimino 'x' del dominio de v1
            domains[v1].remove(x)
            revised = True
            
    return revised

# Algoritmo AC-3
def ac3(variables, domains, constraints):
    # La cola "queue" la lleno con todos los arcos del problema
    queue = list(constraints)
    
    while queue:
        # Saco un arco (v_i, v_j)
        (vi, vj) = queue.pop(0)
        
        # Reviso el arco
        if revise(vi, vj, domains):
            
            # Si el dominio de vi quedó vacío, el CSP no tiene solución
            if not domains[vi]:
                return False # Falla
                
            # Si revisé vi, debo volver a revisar a *sus* vecinos
            # (excepto vj)
            for vk in variables:
                if (vk, vi) in constraints and vk != vj:
                    queue.append((vk, vi))
                    
    return True # Éxito, dominios podados

# --- Ejemplo de uso ---
print(f"Dominios Originales: {domains}")
print("Ejecutando AC-3 para propagar restricciones...")

result = ac3(variables, domains, constraints)

if result:
    print("AC-3 completado.")
    print(f"Dominios Podados: {domains}")
else:
    print("AC-3 falló. El problema no tiene solución.")
    print(f"Dominios Podados: {domains}")

# En este ejemplo, (WA, NT) es revisado.
# Si WA='rojo', NT='rojo' (falla).
# Si WA='verde', NT='rojo' (ok).
#
# Luego se revisa (NT, WA).
# Si NT='rojo', WA puede ser 'verde' (ok).
#
# Luego se revisa (NT, Q).
# Si NT='rojo', Q puede ser 'verde' (ok).
#
# El resultado es que AC-3 no poda nada en este caso simple si
# WA y Q tienen 'verde'. Si WA solo tuviera ['rojo'],
# AC-3 lo detectaría.