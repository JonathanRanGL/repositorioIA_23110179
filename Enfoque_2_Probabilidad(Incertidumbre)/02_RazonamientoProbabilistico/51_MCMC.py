# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #51
# "Monte Carlo para Cadenas de Markov (MCMC - Gibbs Sampling)"

# MCMC es otra forma de inferencia aproximada (como Ponderación).
# Es muy bueno para redes muy grandes y complejas.
#
# Idea (Gibbs Sampling):
# 1. Empezar con un estado (muestra) aleatorio.
# 2. Fijar la evidencia 'e'.
# 3. Repetir N veces:
# 4.   Elegir una variable *no-evidencia* (X_i) al azar.
# 5.   "Re-muestrear" X_i: Borrar su valor actual y asignarle
#      uno nuevo, basado en la probabilidad condicional de X_i
#      dado su *Manto de Markov* actual.
#      P(X_i | Manto(X_i))
# 6. Guardar la muestra (después de un "burn-in").
# 7. Contar los resultados (como en Muestreo por Rechazo).

import random

# --- Ejemplo: Red (Nublado -> Lluvia -> Mojado) ---
# N -> L -> M
# P(N=T) = 0.5
# P(L=T|N=T) = 0.8, P(L=T|N=F) = 0.2
# P(M=T|L=T) = 0.9, P(M=T|L=F) = 0.1
#
# Pregunta: P(L=T | N=T, M=T) ?
# Evidencia: e = {N: True, M: True}
# Variable de consulta: L (esta es la que vamos a re-muestrear)

print("MCMC (Gibbs Sampling)")
print("Estimando P(L=T | N=T, M=T)...")

# CPTs
P_N_T = 0.5
P_L_dado_N = {True: 0.8, False: 0.2}
P_M_dado_L = {True: 0.9, False: 0.1}

# --- 1. Estado inicial aleatorio (fijando evidencia) ---
estado = {
    'N': True, # Evidencia
    'M': True, # Evidencia
    'L': random.choice([True, False]) # Variable oculta
}

N_muestras = 10000
burn_in = 1000
contador_consulta = 0
muestras_guardadas = 0

# --- 3. Bucle de MCMC ---
for i in range(N_muestras + burn_in):
    # 4. Elegir variable no-evidencia (solo 'L')
    var_X = 'L'
    
    # 5. Re-muestrear P(L | Manto(L))
    # Manto(L) = {Padres(L), Hijos(L), Co-Padres(L)}
    # Manto(L) = {N, M} (M no tiene otros padres)
    #
    # Necesitamos P(L | N, M). Por Bayes:
    # P(L | N, M) = alfa * P(L, N, M)
    #             = alfa * P(N) * P(L|N) * P(M|L)
    #
    # Pero P(N) es constante (es evidencia, True).
    # P(L | N, M) = alfa * P(L|N) * P(M|L)  (usando el estado actual)
    
    # Valores actuales del Manto:
    val_N = estado['N'] # True
    val_M = estado['M'] # True
    
    # Calcular P(L=T | N=T, M=T) (proporcional)
    # = P(L=T|N=T) * P(M=T|L=T)
    prob_L_T = P_L_dado_N[val_N] * P_M_dado_L[True] # 0.8 * 0.9 = 0.72
    
    # Calcular P(L=F | N=T, M=T) (proporcional)
    # = P(L=F|N=T) * P(M=T|L=F)
    prob_L_F = P_L_dado_N[val_N] * P_M_dado_L[False] # 0.2 * 0.1 = 0.02
    
    # Normalizar (alfa)
    suma = prob_L_T + prob_L_F
    P_L_T_normalizada = prob_L_T / suma # 0.72 / 0.74 = 0.973
    
    # Re-muestrear L
    if random.random() < P_L_T_normalizada:
        estado['L'] = True
    else:
        estado['L'] = False
        
    # 6. Guardar la muestra (después del burn-in)
    if i >= burn_in:
        muestras_guardadas += 1
        if estado['L'] == True:
            contador_consulta += 1

# 7. Contar resultados
estimacion = contador_consulta / muestras_guardadas
print(f" Muestras totales: {N_muestras + burn_in}, Burn-in: {burn_in}")
print(f" Muestras guardadas: {muestras_guardadas}")
print(f" Muestras (L=T): {contador_consulta}")
print(f" Estimación P(L=T | N=T, M=T) = {estimacion:.4f} (Valor exacto: 0.973)")