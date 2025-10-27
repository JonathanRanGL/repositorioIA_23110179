# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #55
# "Algoritmo Hacia Delante-Atrás (Forward-Backward)"

# Es un algoritmo para resolver la tarea de "Suavizado"
# (Smoothing) en un Modelo Oculto de Markov (HMM).
#
# P(X_k | e_1:t) = alfa * f_k * b_k
#
# f_k = Mensaje "Hacia Adelante" (Forward)
#     f_k = P(X_k, e_1:k)
#     (Calculado recursivamente de 1 a k. Es el FILTRADO)
#
# b_k = Mensaje "Hacia Atrás" (Backward)
#     b_k = P(e_k+1:t | X_k)
#     (Calculado recursivamente de t a k)
#
# alfa = Constante de normalización

# --- Ejemplo HMM: Lluvia (X) y Paraguas (e) ---
# P(X_0) = {Lluvia: 0.5, Sol: 0.5}
# Transición T = P(X_t | X_t-1)
# Observación O = P(e_t | X_t)

# --- Definición Conceptual (Simulación) ---

print("Algoritmo Hacia Delante-Atrás (Conceptual)")
print("Se usa para 'Suavizado': P(X_k | e_1:t)")
print("Combina un pase hacia adelante con uno hacia atrás.")

# Evidencia observada en T=3 días:
# e_1:T = (Paraguas, No Paraguas, Paraguas)
evidencia = [True, False, True]
T_total = 3
k = 2 # Queremos saber P(X_2 | e_1:3)

# --- 1. Pase Hacia Adelante (f) ---
# f_1 = P(X_1, e_1) = P(X_1) * P(e_1 | X_1)
# f_2 = P(X_2, e_1:2) = P(e_2 | X_2) * SUMA_x1( P(X_2 | x1) * f_1(x1) )
#
# (Simulamos los resultados de este cálculo)
f_mensajes = {
    1: {'Lluvia': 0.40, 'Sol': 0.10}, # P(X_1, e_1=T)
    2: {'Lluvia': 0.05, 'Sol': 0.30}, # P(X_2, e_1:2=T,F)
    3: {'Lluvia': 0.03, 'Sol': 0.02}  # P(X_3, e_1:3=T,F,T)
}
print(f"\nMensaje Forward (f) en k=2 (Filtrado):")
print(f"  f_2 = P(X_2, e_1, e_2) = {f_mensajes[2]}")

# --- 2. Pase Hacia Atrás (b) ---
# b_3 = <1, 1> (Vector de unos)
# b_2 = P(e_3 | X_2) = SUMA_x3( P(e_3 | x3) * P(x3 | X_2) * b_3(x3) )
#
# (Simulamos los resultados de este cálculo)
b_mensajes = {
    3: {'Lluvia': 1.0, 'Sol': 1.0},
    2: {'Lluvia': 0.55, 'Sol': 0.30}, # P(e_3=T | X_2)
    1: {'Lluvia': 0.20, 'Sol': 0.40}  # P(e_2:3=F,T | X_1)
}
print(f"\nMensaje Backward (b) en k=2:")
print(f"  b_2 = P(e_3 | X_2) = {b_mensajes[2]}")

# --- 3. Combinación ---
# P(X_2 | e_1:3) = alfa * f_2 * b_2
P_X2_sin_normalizar = {
    'Lluvia': f_mensajes[2]['Lluvia'] * b_mensajes[2]['Lluvia'], # 0.05 * 0.55
    'Sol': f_mensajes[2]['Sol'] * b_mensajes[2]['Sol']       # 0.30 * 0.30
}
# P_X2_sin_normalizar = {'Lluvia': 0.0275, 'Sol': 0.09}

suma_total = sum(P_X2_sin_normalizar.values())
alfa = 1.0 / suma_total

P_X2_normalizado = {
    'Lluvia': P_X2_sin_normalizar['Lluvia'] * alfa,
    'Sol': P_X2_sin_normalizar['Sol'] * alfa
}

print(f"\nResultado (Suavizado) P(X_2 | e_1:3):")
print(f"  f_2 * b_2 (sin normalizar) = {{'Lluvia': {P_X2_sin_normalizar['Lluvia']:.4f}, 'Sol': {P_X2_sin_normalizar['Sol']:.4f}}}")
print(f"  Resultado normalizado: {{'Lluvia': {P_X2_normalizado['Lluvia']:.4f}, 'Sol': {P_X2_normalizado['Sol']:.4f}}}")