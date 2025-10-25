# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #41
# "Distribución de Probabilidad"

# Una distribución de probabilidad es una función (o tabla)
# que describe la probabilidad de *todos los resultados posibles*
# de una variable aleatoria.

# Requisitos:
# 1. Cada probabilidad debe estar entre 0 y 1.
# 2. La suma de todas las probabilidades debe ser 1.

# --- Ejemplo 1: Variable Discreta (Dado de 6 caras) ---
# Variable Aleatoria (X) = "Resultado de lanzar un dado"
# Dominio = {1, 2, 3, 4, 5, 6}

distribucion_dado_justo = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

print("Distribución de Probabilidad (Variable Discreta)")
print(f"Distribución de un dado justo: {distribucion_dado_justo}")
print(f"Suma de probabilidades: {sum(distribucion_dado_justo.values())}")

# Un dado cargado también tiene una distribución
distribucion_dado_cargado = {
    1: 0.1,
    2: 0.1,
    3: 0.1,
    4: 0.1,
    5: 0.1,
    6: 0.5  # Cargado al 6
}
print(f"\nDistribución de un dado cargado: {distribucion_dado_cargado}")
print(f"Suma de probabilidades: {sum(distribucion_dado_cargado.values())}")


# --- Ejemplo 2: Variable Continua ---
# Variable Aleatoria (Y) = "Temperatura de mañana"
# Dominio = (infinito, -infinito)
#
# No podemos asignar una probabilidad a Y=20.50000...
# (La prob. de un valor exacto es 0).
#
# Usamos una "Función de Densidad de Probabilidad" (PDF),
# como la Distribución Normal (Gaussiana).
#
# P(20 <= Y <= 21) = (Integral de la PDF de 20 a 21)

print("\nDistribución de Probabilidad (Variable Continua)")
print("Se usa una Función de Densidad (PDF), ej. Normal(media, std_dev)")
print("La probabilidad se mide en *rangos* (ej. P(20 < T < 21)).")