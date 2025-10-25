# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #40
# "Probabilidad Condicionada y Normalización"

# --- Probabilidad Condicionada P(A|B) ---
# "La probabilidad de A, *dado que* sabemos que B es verdadero."
#
# Fórmula: P(A|B) = P(A y B) / P(B)
#
# P(A y B) = Probabilidad conjunta (prob. de que ambos pasen)
# P(B)     = Probabilidad a priori de la evidencia

# --- Ejemplo: Nubes y Lluvia ---
#
# P(Lluvia) = 0.1 (Prior)
# P(Nubes) = 0.4 (Prior)
# P(Lluvia y Nubes) = 0.08 (Prob. conjunta)
#
# Pregunta: ¿Cuál es la prob. de que llueva, *dado que* vemos nubes?
# P(Lluvia | Nubes) = ?

P_Lluvia_y_Nubes = 0.08
P_Nubes = 0.4

P_Lluvia_dado_Nubes = P_Lluvia_y_Nubes / P_Nubes

print("Probabilidad Condicionada P(A|B)")
print(f"P(Lluvia | Nubes) = P(Lluvia y Nubes) / P(Nubes)")
print(f"P(Lluvia | Nubes) = {P_Lluvia_y_Nubes} / {P_Nubes} = {P_Lluvia_dado_Nubes}")
print("Saber que hay nubes sube la prob. de lluvia de 0.1 a 0.2\n")


# --- Normalización ---
#
# A veces no conocemos P(B) (la evidencia, P(Nubes)).
# Pero podemos calcular P(Lluvia | Nubes) y P(No Lluvia | Nubes)
# de forma proporcional.
#
# P(A|B) = alfa * P(A y B)
#
# "alfa" es una constante de normalización que asegura que
# la suma de probabilidades dé 1.
# alfa = 1 / P(B)

# Ejemplo:
# P(Lluvia y Nubes) = 0.08
# P(No Lluvia y Nubes) = 0.32
#
# (Nota: P(Nubes) = 0.08 + 0.32 = 0.40, lo que ya sabíamos)

# Creamos un vector de probabilidades (sin normalizar)
P_Clima_dado_Nubes_sin_normalizar = {
    'Lluvia': 0.08,  # P(Lluvia y Nubes)
    'No Lluvia': 0.32 # P(No Lluvia y Nubes)
}

# Calculamos alfa (que es 1 / suma_de_probabilidades)
suma_total = sum(P_Clima_dado_Nubes_sin_normalizar.values())
alfa = 1.0 / suma_total

# Normalizamos
P_Clima_dado_Nubes_normalizado = {
    'Lluvia': P_Clima_dado_Nubes_sin_normalizar['Lluvia'] * alfa,
    'No Lluvia': P_Clima_dado_Nubes_sin_normalizar['No Lluvia'] * alfa
}

print("Normalización")
print(f"Vector sin normalizar P(Clima, Nubes): {P_Clima_dado_Nubes_sin_normalizar}")
print(f"Suma (esto es P(Nubes)): {suma_total}")
print(f"Constante alfa (1 / {suma_total}): {alfa}")
print(f"Vector normalizado P(Clima | Nubes): {P_Clima_dado_Nubes_normalizado}")
print(f"Suma final: {sum(P_Clima_dado_Nubes_normalizado.values())}")