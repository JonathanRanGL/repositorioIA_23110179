# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #24
# "Teoría de la Utilidad: Función de Utilidad"

import math

# La "utilidad" no es el dinero en sí, sino la "satisfacción" que produce.
# Un agente "adverso al riesgo" prefiere una ganancia segura
# a una apuesta con una ganancia esperada igual o mayor.
# Esto se modela con una función de utilidad cóncava (ej. logaritmo, raíz).

# Función de utilidad para un agente adverso al riesgo (U(x) = sqrt(x))
def utility_risk_averse(money):
    # Evita errores con valores negativos
    if money < 0:
        return -utility_risk_averse(-money) 
    return math.sqrt(money)

# Función de utilidad para un agente neutral al riesgo (U(x) = x)
def utility_risk_neutral(money):
    return money

# --- Ejemplo de decisión ---
# Dos opciones:
# 1. Ganancia segura: $400
# 2. Apuesta: 50% de ganar $1000, 50% de ganar $0
#
# Valor Esperado (VE) de la apuesta:
# VE = (0.5 * $1000) + (0.5 * $0) = $500
#
# Un agente neutral (que solo ve el VE) tomaría la apuesta ($500 > $400).

# --- Cálculo de Utilidad Esperada (UE) ---

print("Calculando la Utilidad Esperada (UE)...")

# 1. Para el Agente NEUTRAL al riesgo (U(x) = x)
u_segura_neutral = utility_risk_neutral(400)
u_apuesta_neutral = (0.5 * utility_risk_neutral(1000)) + (0.5 * utility_risk_neutral(0))
print(f"Agente Neutral: U(Segura, $400) = {u_segura_neutral}")
print(f"Agente Neutral: U(Apuesta, $500 VE) = {u_apuesta_neutral}")
if u_apuesta_neutral > u_segura_neutral:
    print("  -> Decisión Neutral: Tomar la apuesta.")
else:
    print("  -> Decisión Neutral: Tomar el dinero seguro.")

# 2. Para el Agente ADVERSO al riesgo (U(x) = sqrt(x))
u_segura_adversa = utility_risk_averse(400)
u_apuesta_adversa = (0.5 * utility_risk_averse(1000)) + (0.5 * utility_risk_averse(0))
print(f"\nAgente Adverso: U(Segura, $400) = {u_segura_adversa:.2f}")
print(f"Agente Adverso: U(Apuesta) = {u_apuesta_adversa:.2f}")

# Comparamos: U(Apuesta) = 15.81, U(Segura $400) = 20.0
# La utilidad de la apuesta (15.81) es MENOR que la utilidad del dinero seguro (20.0)
if u_apuesta_adversa > u_segura_adversa:
    print("  -> Decisión Adversa: Tomar la apuesta.")
else:
    print("  -> Decisión Adversa: Tomar el dinero seguro.")