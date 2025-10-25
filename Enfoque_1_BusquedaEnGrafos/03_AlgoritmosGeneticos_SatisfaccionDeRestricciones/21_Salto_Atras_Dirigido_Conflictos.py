# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #21
# "Salto Atrás Dirigido por Conflictos (CBJ) - Concepto"

# CBJ es una versión más inteligente de Backtracking.
#
# Backtracking estándar:
# 1. Asigno A='rojo'
# 2. Asigno B='verde'
# 3. Asigno C='azul'
# 4. Intento asignar D... pero todos sus valores fallan.
# 5. Backtracking "vuelve atrás" a C y le cambia el color.
#
# Problema: ¿Qué pasa si el fallo en D no fue culpa de C,
# sino culpa de A ('rojo')? Backtracking probará todos los
# colores de C inútilmente antes de volver a A.
#
# Salto Atrás Dirigido por Conflictos (CBJ):
# 1. Mantiene un "conjunto de conflictos" para cada variable.
# 2. Asigno A (conflicto={})
# 3. Asigno B (conflicto={})
# 4. Asigno C (conflicto={})
# 5. Intento asignar D:
#    - D='rojo' falla por A. (Conflicto de D ahora es {A})
#    - D='verde' falla por B. (Conflicto de D ahora es {A, B})
# 6. D falla. En lugar de volver a C (la variable anterior),
#    CBJ mira el conjunto de conflictos {A, B} y "salta"
#    directamente a la variable más reciente en ese conjunto (B).
#    Y le pasa el conflicto {A} a B.

# Este es un algoritmo conceptual. Implementarlo es complejo.
# El siguiente código *simula* la lógica de decisión de CBJ.

def simulate_cbj():
    print("Simulación de Salto Atrás Dirigido por Conflictos (CBJ)")
    
    # Variables a asignar: A, B, C, D, E
    assignment = {}
    
    # 1. Asignar A, B, C
    assignment['A'] = 'rojo'
    assignment['B'] = 'verde'
    assignment['C'] = 'azul'
    print(f"Asignado: {assignment}")
    
    # 2. Intentar asignar D
    print("\nIntentando asignar D...")
    # Supongamos que las restricciones son:
    # D != A ('rojo')
    # D != B ('verde')
    # Dominio de D = ['rojo', 'verde']
    
    conflict_set_D = set()
    
    # Intento D = 'rojo'
    print("  Probando D = 'rojo'... Falla (conflicto con A)")
    conflict_set_D.add('A')
    
    # Intento D = 'verde'
    print("  Probando D = 'verde'... Falla (conflicto con B)")
    conflict_set_D.add('B')
    
    # 3. D falla. No hay más valores.
    print(f"\nFallo en D. Conjunto de conflictos de D: {conflict_set_D}")
    
    # 4. Decisión de Backtrack vs CBJ
    
    # Backtracking estándar:
    print("  Backtracking estándar volvería a 'C'.")
    
    # CBJ:
    # El conjunto es {A, B}. La variable más reciente es 'B'.
    print(f"  CBJ 'salta' directamente a 'B' (ignora 'C').")
    
    # CBJ pasaría el conflicto {A} a B, indicando que B
    # debe cambiar de valor *sin* que A sea la causa del fallo.
    
    print("\nCBJ evita probar todos los valores de 'C' inútilmente,")
    print("ya que 'C' no tenía nada que ver con el fallo de 'D'.")

# --- Ejemplo de uso ---
simulate_cbj()