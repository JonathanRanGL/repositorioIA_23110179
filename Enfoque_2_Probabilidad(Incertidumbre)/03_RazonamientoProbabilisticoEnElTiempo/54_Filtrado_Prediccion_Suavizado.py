# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #54
# "Filtrado, Predicción, Suavizado y Explicación"

# Estas son las 4 tareas principales de inferencia
# en modelos temporales (como HMMs o Filtros de Kalman).
#
# Evidencia (e) = {e_1, e_2, ..., e_t} (Lo que observamos)
# Estado (X) = {X_1, X_2, ..., X_t} (Lo que queremos saber)

print("Tareas de Inferencia en Modelos Temporales:")

# --- 1. Filtrado ---
# P(X_t | e_1:t)
# ¿Cuál es el estado del sistema AHORA (t),
#  dada toda la evidencia HASTA AHORA (1 a t)?
#
# (Ej. ¿Dónde está el robot *ahora*, basado en todas
#  las lecturas del sensor hasta este momento?)
# (Usado para: Seguimiento en tiempo real)
print("\n1. Filtrado: P(X_t | e_1:t)")
print("   ¿Cuál es el estado AHORA?")
print("   (Se usa la 'Observación' de hoy para corregir la 'Predicción' de ayer)")

# --- 2. Predicción ---
# P(X_t+k | e_1:t)  (donde k > 0)
# ¿Cuál será el estado del sistema en el FUTURO (t+k),
#  dada toda la evidencia HASTA AHORA (1 a t)?
#
# (Ej. ¿Dónde estará el robot en 5 segundos?)
print("\n2. Predicción: P(X_t+k | e_1:t)")
print("   ¿Cuál será el estado en el FUTURO?")
print("   (Se proyecta el estado actual hacia adelante sin nueva evidencia)")

# --- 3. Suavizado (Smoothing) ---
# P(X_k | e_1:t)  (donde 0 < k < t)
# ¿Cuál *era* el estado del sistema en el PASADO (k),
#  dada toda la evidencia HASTA HOY (1 a t)?
#
# (Ej. Revisando la telemetría del día, ¿dónde *estaba*
#  el robot a las 10:00 AM?)
# (Es más preciso que el filtrado, porque usa evidencia "futura")
print("\n3. Suavizado (Smoothing): P(X_k | e_1:t), k < t")
print("   ¿Cuál *era* el estado en el PASADO?")
print("   (Re-calcula una estimación pasada usando nueva evidencia)")

# --- 4. Explicación (Most Likely Explanation) ---
# argmax(x_1:t) P(x_1:t | e_1:t)
# ¿Cuál es la *secuencia completa* de estados más probable
#  que explique *toda* la evidencia?
#
# (Ej. Dada la grabación de audio, ¿qué *secuencia* de
#  fonemas (palabras) es la más probable?)
# (Se usa el Algoritmo de Viterbi)
print("\n4. Explicación (Most Likely Explanation): argmax P(x_1:t | e_1:t)")
print("   ¿Cuál es la SECUENCIA de estados más probable?")
print("   (Resuelto por el Algoritmo de Viterbi)")