# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #29
# "Proceso de Decisión de Markov (MDP) - Concepto"

# Un MDP es un *marco* para tomar decisiones en un entorno
# estocástico (con probabilidades).
# No es un algoritmo en sí, sino el *problema* que
# algoritmos como "Iteración de Valores" o "Q-Learning" resuelven.

# Un MDP se define por 5 componentes: (S, A, P, R, gamma)

# 1. S: Conjunto de Estados
#    (Posiciones en un mapa, niveles de inventario, etc.)
S = ['Bueno', 'Malo', 'Meta']

# 2. A: Conjunto de Acciones
#    (Moverse, Comprar, Esperar, etc.)
A = ['Intentar', 'Descansar']

# 3. P: Modelo de Transición (Probabilidad)
#    P(s' | s, a)
#    "La probabilidad de terminar en el estado s' (siguiente),
#     si estoy en el estado s y tomo la acción a."
#
# P( 'Bueno' | 'Bueno', 'Intentar' ) = 0.7
# P( 'Malo'  | 'Bueno', 'Intentar' ) = 0.3
# P( 'Meta'  | 'Bueno', 'Intentar' ) = 0.0
# ... etc.
#
# (Esto se representa como una gran tabla o función)
P = {
    'Bueno': {
        'Intentar': [('Bueno', 0.7), ('Malo', 0.3), ('Meta', 0.0)],
        'Descansar': [('Bueno', 1.0), ('Malo', 0.0), ('Meta', 0.0)]
    },
    'Malo': {
        'Intentar': [('Bueno', 0.2), ('Malo', 0.7), ('Meta', 0.1)],
        'Descansar': [('Bueno', 0.0), ('Malo', 1.0), ('Meta', 0.0)]
    },
    'Meta': { # Estado terminal
        'Intentar': [('Meta', 1.0)],
        'Descansar': [('Meta', 1.0)]
    }
}

# 4. R: Modelo de Recompensa
#    R(s)
#    "La recompensa (o costo) que recibo por estar en el estado s."
R = {
    'Bueno': 5,
    'Malo': -10,
    'Meta': 100
}

# 5. Gamma (y)
#    Factor de Descuento (entre 0 y 1)
#    "Cuánto valoro las recompensas futuras comparadas con las inmediatas."
#    gamma = 0.9 -> "Importa mucho el futuro"
#    gamma = 0.1 -> "Solo importa el corto plazo (miope)"
gamma = 0.9

print("Definición de un Proceso de Decisión de Markov (MDP)")
print("El objetivo es encontrar una 'Política' pi(s) -> a")
print("que maximice la recompensa total descontada esperada.")
print("\nComponentes:")
print(f"S (Estados): {S}")
print(f"A (Acciones): {A}")
print(f"R (Recompensas): {R}")
print(f"Gamma (Descuento): {gamma}")
print(f"P (Transición de 'Malo' con 'Intentar'): {P['Malo']['Intentar']}")