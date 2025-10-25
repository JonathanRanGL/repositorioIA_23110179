# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #26
# "Valor de la Información (VPI)"

# ¿Cuánto vale la pena pagar por obtener más información (ej. un pronóstico)?
# VPI = MEU(con información) - MEU(sin información)

# --- Usando el ejemplo del Paraguas (Algoritmo 25) ---

# 1. MEU (sin información)
# Del cálculo anterior, la MEU sin saber el pronóstico es 70
MEU_sin_info = 70.0
print(f"MEU (sin información) = {MEU_sin_info}")

# 2. MEU (con información)
# Asumimos que obtenemos un "Pronóstico Perfecto" (VPI perfecto).
# El pronóstico nos dirá *exactamente* si va a llover o no.
#
# Hay dos casos para el pronóstico:
#   A. El pronóstico dice "Lluvia" (Esto pasará con P=0.3)
#   B. El pronóstico dice "No Lluvia" (Esto pasará con P=0.7)

# Caso A: Pronóstico dice "Lluvia".
#   Sabemos que lloverá. ¿Cuál es nuestra mejor decisión?
#   U(Lluvia, Tomar) = 70
#   U(Lluvia, No Tomar) = 0
#   -> Decisión si "Lluvia": Tomar paraguas (Utilidad = 70)

# Caso B: Pronóstico dice "No Lluvia".
#   Sabemos que no lloverá. ¿Cuál es nuestra mejor decisión?
#   U(NoLluvia, Tomar) = 20
#   U(NoLluvia, No Tomar) = 100
#   -> Decisión si "No Lluvia": No tomar paraguas (Utilidad = 100)

# La MEU *con* información es el promedio ponderado de la utilidad
# que obtendremos en cada caso del pronóstico.

P_Lluvia = 0.3
P_NoLluvia = 0.7

MEU_con_info = (P_Lluvia * 70) + (P_NoLluvia * 100)
# MEU_con_info = (0.3 * 70) + (0.7 * 100)
# MEU_con_info = 21 + 70 = 91

print(f"MEU (con información perfecta) = {MEU_con_info}")

# 3. Calcular el Valor de la Información Perfecta (VPI)
VPI = MEU_con_info - MEU_sin_info
# VPI = 91 - 70 = 21

print(f"\nValor de la Información Perfecta (VPI) = {VPI}")
print("Vale la pena pagar hasta 21 'puntos de utilidad' por un pronóstico perfecto.")