# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #57
# "Filtros de Kalman"

# Un Filtro de Kalman es la solución para un HMM
# que cumple con tres condiciones:
# 1. Los estados (X) son *continuos* (ej. posición, velocidad).
# 2. Las observaciones (E) son *continuas*.
# 3. Los modelos (Transición y Observación) son *lineales*.
# 4. La incertidumbre (ruido) es *Gaussiana* (Normal).
#
# Es el algoritmo óptimo para "Filtrado" en estos casos.
# (Ej. Rastrear un misil, estimar la posición de un coche).
#
# Funciona en un ciclo de dos pasos:
# 1. Predecir: Proyecta el estado y la incertidumbre (covarianza)
#    hacia el futuro (t+1).
# 2. Actualizar: Corrige la predicción usando la nueva
#    observación (medición) del sensor en t+1.

import numpy as np

# --- Ejemplo 1D: Rastrear un objeto con posición (x) ---
# Estado (x) = [posición, velocidad]
# Observación (z) = [posición_medida]

print("Filtro de Kalman (Simulación 1D)")

# 1. Definir el estado inicial
# (Posición=0, Velocidad=1)
x = np.array([[0.0], [1.0]])
# Incertidumbre inicial (Covarianza P)
P = np.array([[1.0, 0.0], [0.0, 1.0]])

# 2. Definir los Modelos Lineales
dt = 1.0 # 1 segundo por paso

# A = Matriz de Transición (Cómo cambia x)
# x_t = A * x_t-1
# pos = pos + vel*dt
# vel = vel
A = np.array([[1.0, dt], [0.0, 1.0]])

# H = Matriz de Observación (Cómo se relaciona x con z)
# z_t = H * x_t
# pos_medida = 1*pos + 0*vel
H = np.array([[1.0, 0.0]])

# 3. Definir el Ruido (Incertidumbre Gaussiana)
# R = Ruido de la medición (Sensor)
R = np.array([[10.0]]) # Sensor ruidoso
# Q = Ruido del proceso (Movimiento)
Q = np.array([[0.1, 0.0], [0.0, 0.1]]) # Movimiento un poco errático

# --- Simulación (3 pasos) ---
mediciones = [1.1, 1.9, 3.2] # Mediciones z
print(f"Estado inicial (x_0): pos={x[0,0]:.2f}, vel={x[1,0]:.2f}")

for i, z in enumerate(mediciones):
    
    # --- 1. PREDECIR ---
    # x_pred = A * x_actual
    x_pred = A @ x
    # P_pred = A * P_actual * A.T + Q
    P_pred = (A @ P @ A.T) + Q
    
    # --- 2. ACTUALIZAR (Corregir con la medición z) ---
    
    # Ganancia de Kalman (K)
    # K = P_pred * H.T * inv(H * P_pred * H.T + R)
    K_numerador = P_pred @ H.T
    K_denominador = (H @ P_pred @ H.T) + R
    K = K_numerador @ np.linalg.inv(K_denominador)
    
    # Corregir estado (x)
    # y = z - H * x_pred (El "error" o "sorpresa")
    y = z - (H @ x_pred)
    x = x_pred + (K @ y)
    
    # Corregir incertidumbre (P)
    # P = (I - K * H) * P_pred
    I = np.eye(2)
    P = (I - (K @ H)) @ P_pred
    
    print(f"\nPaso {i+1}: Medición (z={z:.2f})")
    print(f"  Estimación (x_{i+1}): pos={x[0,0]:.2f}, vel={x[1,0]:.2f}")
    print(f"  Incertidumbre (P) diagonal: {P.diagonal()}")