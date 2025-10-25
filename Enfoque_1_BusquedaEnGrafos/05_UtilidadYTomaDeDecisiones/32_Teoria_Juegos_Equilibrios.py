# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #32
# "Teoría de Juegos: Equilibrios y Mecanismos"

# La Teoría de Juegos modela la toma de decisiones estratégicas
# entre múltiples agentes.
#
# Un "Equilibrio de Nash" es un estado del juego donde ningún
# jugador puede beneficiarse cambiando *solo* su propia estrategia,
# asumiendo que los demás no cambian.

# --- Ejemplo: El Dilema del Prisionero ---
#
# Dos prisioneros (A y B). Opciones: Confesar o Callar.
#
# Matriz de Pagos (Utilidad): (Pago_A, Pago_B)
# (Los pagos son "años de cárcel", así que números más bajos son mejores)
#
#                 Prisionero B
#               Confesar     Callar
# A Confesar   (-5, -5)     (0, -10)
# A Callar     (-10, 0)     (-1, -1)
#

# Definimos la matriz de pagos
# payoffs[A_accion][B_accion] = (Pago_A, Pago_B)
payoffs = {
    'Confesar': {
        'Confesar': (-5, -5),
        'Callar': (0, -10)
    },
    'Callar': {
        'Confesar': (-10, 0),
        'Callar': (-1, -1)
    }
}
actions_A = ['Confesar', 'Callar']
actions_B = ['Confesar', 'Callar']

# --- Algoritmo para encontrar Equilibrios de Nash (en estrategias puras) ---
print("Buscando Equilibrio de Nash en el Dilema del Prisionero...")
print("Pagos (A, B) | Más bajo es mejor (años de cárcel)")

equilibriums = []

# Itero sobre todas las combinaciones de estrategias posibles
for a_A in actions_A:
    for a_B in actions_B:
        
        current_payoff_A, current_payoff_B = payoffs[a_A][a_B]
        
        # 1. Comprobar si A tiene un incentivo para cambiar
        #    (Asumiendo que B *mantiene* su acción a_B)
        A_can_improve = False
        for other_a_A in actions_A:
            if other_a_A == a_A:
                continue
            
            # Compara su pago actual con el pago si cambiara
            new_payoff_A, _ = payoffs[other_a_A][a_B]
            if new_payoff_A > current_payoff_A: # (Cambiamos > por < para este problema)
                A_can_improve = True
                break
        
        # 2. Comprobar si B tiene un incentivo para cambiar
        #    (Asumiendo que A *mantiene* su acción a_A)
        B_can_improve = False
        for other_a_B in actions_B:
            if other_a_B == a_B:
                continue
                
            _, new_payoff_B = payoffs[a_A][other_a_B]
            if new_payoff_B > current_payoff_B: # (Cambiamos > por < para este problema)
                B_can_improve = True
                break
                
        # 3. Si *ninguno* de los dos puede mejorar, es un Equilibrio de Nash
        if not A_can_improve and not B_can_improve:
            equilibriums.append((a_A, a_B))
            
# --- Resultados ---
if equilibriums:
    print(f"\nEquilibrios de Nash encontrados:")
    for eq in equilibriums:
        print(f"  - A: {eq[0]}, B: {eq[1]} -> Pago: {payoffs[eq[0]][eq[1]]}")
else:
    print("\nNo se encontraron Equilibrios de Nash en estrategias puras.")

# (El resultado es (Confesar, Confesar) -> -5, -5)
# Aunque (Callar, Callar) -> (-1, -1) es "mejor" para ambos,
# no es un equilibrio estable, porque si B decide Callar,
# A tiene un incentivo para traicionarlo y Confesar (0 > -1)).