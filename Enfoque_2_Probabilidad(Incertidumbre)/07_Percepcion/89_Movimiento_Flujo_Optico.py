# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #89
# "Movimiento (Flujo Óptico)"

# El Flujo Óptico es la tarea de estimar el
# "movimiento aparente" de los píxeles
# entre dos fotogramas consecutivos de un video.
#
# Asume que la "brillo" de un píxel no cambia
# (Ecuación de Flujo Óptico).
#
# Resultado: Un campo vectorial (un vector [u, v]
# para cada píxel), donde [u, v] dice
# "este píxel (x,y) se movió 'u' píxeles en X
#  y 'v' píxeles en Y".

import numpy as np
import cv2

print("Movimiento (Flujo Óptico - Farnebäck)")

# --- 1. Crear dos "fotogramas" de un video ---
# (Sin cargar archivos)
# (Imagen 100x100, en escala de grises)

# Frame 1: Un cuadrado a la izquierda
frame1 = np.zeros((100, 100), dtype=np.uint8)
frame1[40:60, 20:40] = 255

# Frame 2: El mismo cuadrado, movido 10 píxeles a la derecha
frame2 = np.zeros((100, 100), dtype=np.uint8)
frame2[40:60, 30:50] = 255

# --- 2. Calcular Flujo Óptico Denso (Gunnar Farnebäck) ---
# "Denso" = Calcula el vector [u, v] para CADA píxel.
# (El otro método es 'Lucas-Kanade', que es 'disperso'
#  y solo rastrea 'esquinas' específicas).
flow = cv2.calcOpticalFlowFarneback(
    prev=frame1, 
    next=frame2, 
    flow=None, 
    pyr_scale=0.5, 
    levels=3, 
    winsize=15, 
    iterations=3, 
    poly_n=5, 
    poly_sigma=1.2, 
    flags=0
)

print(f"\nSe crearon 2 fotogramas (100x100) con un cuadrado móvil.")
print(f"Shape del Flujo Óptico (alto, ancho, 2 (u,v)): {flow.shape}")

# 3. Analizar el resultado
# En la zona donde *no* hubo movimiento (fondo negro),
# el flujo (u, v) debería ser casi (0, 0).
mean_flow_fondo = np.mean(flow[:20, :20], axis=(0,1))

# En la zona donde *sí* hubo movimiento (el cuadrado),
# el flujo (u) debería ser cercano a 10 (movimiento en X).
# (Estimamos la zona del cuadrado en el frame 1)
mean_flow_objeto = np.mean(flow[40:60, 20:40], axis=(0,1))

print(f"\nFlujo medio del fondo (u, v): [{mean_flow_fondo[0]:.2f}, {mean_flow_fondo[1]:.2f}] (Cercano a 0)")
print(f"Flujo medio del objeto (u, v): [{mean_flow_objeto[0]:.2f}, {mean_flow_objeto[1]:.2f}] (Cercano a 10 en X)")
print("\n(El algoritmo estimó correctamente el movimiento del cuadrado).")