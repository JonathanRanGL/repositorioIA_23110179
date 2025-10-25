# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #25
# "Redes de Decisión (MEU)"

# Una Red de Decisión (o Diagrama de Influencia) es una Red Bayesiana
# que incluye nodos de Decisión (rectángulos) y nodos de Utilidad (diamantes).
#
# Objetivo: Encontrar la "Máxima Utilidad Esperada" (MEU).

# --- Ejemplo: ¿Llevar paraguas? ---
#
# Nodos de Azar (Variables):
#   - Clima (Lluvia=0.3, No Lluvia=0.7)
#
# Nodos de Decisión:
#   - Paraguas (Tomar, No Tomar)
#
# Nodos de Utilidad (depende de la combinación de Clima y Decisión):
#   U(Lluvia, Tomar)     = 70  (Ok, un poco incómodo)
#   U(Lluvia, No Tomar)   = 0   (Empapado, muy mal)
#   U(No Lluvia, Tomar)  = 20  (Incómodo cargar el paraguas)
#   U(No Lluvia, No Tomar)= 100 (Perfecto)

# Probabilidades
P_Lluvia = 0.3
P_NoLluvia = 0.7

# Tabla de Utilidad
U = {
    ('Lluvia', 'Tomar'): 70,
    ('Lluvia', 'No Tomar'): 0,
    ('NoLluvia', 'Tomar'): 20,
    ('NoLluvia', 'No Tomar'): 100
}

# 1. Calcular la Utilidad Esperada (UE) de cada *decisión*

# UE(Decisión) = SUMA [ P(Estado) * U(Estado, Decisión) ]
#                (sobre todos los estados posibles del "padre" de la utilidad)

# UE para la decisión "Tomar Paraguas"
UE_Tomar = (P_Lluvia * U[('Lluvia', 'Tomar')]) + (P_NoLluvia * U[('NoLluvia', 'Tomar')])
# UE_Tomar = (0.3 * 70) + (0.7 * 20)
# UE_Tomar = 21 + 14 = 35

# UE para la decisión "No Tomar Paraguas"
UE_NoTomar = (P_Lluvia * U[('Lluvia', 'No Tomar')]) + (P_NoLluvia * U[('NoLluvia', 'No Tomar')])
# UE_NoTomar = (0.3 * 0) + (0.7 * 100)
# UE_NoTomar = 0 + 70 = 70

print("Calculando la Máxima Utilidad Esperada (MEU)...")
print(f"Utilidad Esperada (UE) de 'Tomar Paraguas': {UE_Tomar}")
print(f"Utilidad Esperada (UE) de 'No Tomar Paraguas': {UE_NoTomar}")

# 2. Elegir la decisión con la MEU (Máxima Utilidad Esperada)
if UE_Tomar > UE_NoTomar:
    MEU = UE_Tomar
    Decision = "Tomar Paraguas"
else:
    MEU = UE_NoTomar
    Decision = "No Tomar Paraguas"

print(f"\nDecisión Óptima: {Decision}")
print(f"MEU: {MEU}")