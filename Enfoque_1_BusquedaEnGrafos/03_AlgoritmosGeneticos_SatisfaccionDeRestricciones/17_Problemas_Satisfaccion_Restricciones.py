# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #17
# "Problemas de Satisfacción de Restricciones (CSP) - Concepto"

# Un CSP se define por tres componentes:
# 1. Variables: Las "incógnitas" que debemos resolver.
# 2. Dominios: El conjunto de posibles valores que cada variable puede tomar.
# 3. Restricciones: Las reglas que definen qué combinaciones de valores son válidas.

# --- Ejemplo: Coloración de un Mapa (Australia) ---

# 1. Variables
# (Representan los territorios)
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

# 2. Dominios
# (Los colores que cada territorio puede tomar)
# Cada variable tiene el mismo dominio inicial.
domains = {
    'WA': ['rojo', 'verde', 'azul'],
    'NT': ['rojo', 'verde', 'azul'],
    'Q':  ['rojo', 'verde', 'azul'],
    'NSW':['rojo', 'verde', 'azul'],
    'V':  ['rojo', 'verde', 'azul'],
    'SA': ['rojo', 'verde', 'azul'],
    'T':  ['rojo', 'verde', 'azul']
}

# 3. Restricciones
# (Pares de territorios que son vecinos y no pueden tener el mismo color)
# (Ej: 'SA' no puede ser igual a 'WA')
constraints = [
    ('SA', 'WA'), ('SA', 'NT'), ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'),
    ('WA', 'NT'),
    ('NT', 'Q'),
    ('Q', 'NSW'),
    ('NSW', 'V')
]

# Una "solución" a este CSP es una "asignación" de un color a cada
# variable (territorio) de tal manera que ninguna restricción se viole.
#
# Ejemplo de solución válida:
# {'WA': 'rojo', 'NT': 'verde', 'Q': 'rojo', 'NSW': 'verde', 
#  'V': 'rojo', 'SA': 'azul', 'T': 'rojo'}

print("Ejemplo de definición de un Problema de Satisfacción de Restricciones (CSP)")
print(f"Variables: {variables}")
print(f"Dominio de 'WA': {domains['WA']}")
print(f"Restricción (vecinos): {constraints[0]}")
print("\nEl objetivo es encontrar una asignación (color) para cada variable")
print("respetando todas las restricciones.")