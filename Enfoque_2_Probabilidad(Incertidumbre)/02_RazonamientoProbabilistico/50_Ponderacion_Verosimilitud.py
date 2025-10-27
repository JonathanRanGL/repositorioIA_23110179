# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #50
# "Ponderación de Verosimilitud (Likelihood Weighting)"

# Es una mejora al Muestreo por Rechazo.
# Problema: Si la evidencia 'e' es muy rara, Rechazo
# ignora casi todas las muestras. Es ineficiente.
#
# Ponderación de Verosimilitud:
# 1. Fija el valor de las variables de evidencia 'e'.
# 2. Muestrea solo las variables restantes (padres, hijos).
# 3. Pesa cada muestra por la "verosimilitud" (likelihood)
#    de la evidencia, dado lo que muestreó de los padres.
#
# w = PRODUCTO [ P(e_i | Padres(e_i)) ]
#     (para cada variable e_i en la evidencia e)

import random

# --- Ejemplo: Red (Lluvia -> Mojado) ---
# P(L) = {T: 0.3}
# P(M | L=T) = 0.9
# P(M | L=F) = 0.2
#
# Pregunta: P(L=T | M=T) ?
# Evidencia (e) = M=T

def ponderacion_verosimilitud():
    # Inicializo el peso de la muestra
    w = 1.0
    
    # 1. Muestrear variables que NO son evidencia
    #    (La variable 'L' no es evidencia)
    if random.random() < 0.3: # P(L=T)
        L = True
    else:
        L = False
        
    # 2. Fijar la evidencia (M=T) y calcular su peso
    #    La variable 'M' ES evidencia (M=T).
    #    No la muestreamos. Calculamos su 'peso'
    #    basado en su padre ('L', que sí muestreamos).
    
    if L == True:
        # w = w * P(M=T | L=T)
        w = w * 0.9
    else: # L == False
        # w = w * P(M=T | L=F)
        w = w * 0.2
        
    # La muestra es (L_muestreada, peso_w)
    return (L, w)

print("Ponderación de Verosimilitud")
print("Estimando P(L=T | M=T)...")

N_muestras = 10000
# Usamos dos contadores (ponderados)
total_peso_T = 0.0 # Acumulador para L=T
total_peso_F = 0.0 # Acumulador para L=F

for _ in range(N_muestras):
    (L, w) = ponderacion_verosimilitud()
    
    # Acumulo el peso en el contador correspondiente
    if L == True:
        total_peso_T += w
    else:
        total_peso_F += w

# El resultado es la normalización de los pesos
suma_total_pesos = total_peso_T + total_peso_F
if suma_total_pesos > 0:
    estimacion_T = total_peso_T / suma_total_pesos
    estimacion_F = total_peso_F / suma_total_pesos
    print(f" Muestras generadas: {N_muestras} (Ninguna se rechaza)")
    print(f" Peso acumulado (L=T): {total_peso_T:.2f}")
    print(f" Peso acumulado (L=F): {total_peso_F:.2f}")
    print(f"\n Estimación P(L=T | M=T) = {estimacion_T:.4f}")
    print(f" Estimación P(L=F | M=T) = {estimacion_F:.4f}")
    print(f" (Valor exacto del Algoritmo 47: 0.6585)")