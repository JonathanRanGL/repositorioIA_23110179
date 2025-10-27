# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #52
# "Procesos Estacionarios"

# Un proceso estocástico (que cambia con el tiempo) es
# "estacionario" si sus propiedades estadísticas
# (como la media y la varianza) no cambian con el tiempo.

# --- Ejemplo 1: Proceso Estacionario ---
# Lanzar un dado justo.
# P(Dado=6) es 1/6.
# La media del resultado (3.5) es siempre 3.5.
# No importa si lo lanzo hoy o en 10 años, la
# distribución de probabilidad es la misma.

print("Proceso Estacionario (Ej: Lanzar un dado justo)")
prob_dado = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
media_dado = sum(k * v for k, v in prob_dado.items())
print(f"  Media en t=1: {media_dado}")
print(f"  Media en t=100: {media_dado} (No cambia)")

# --- Ejemplo 2: Proceso NO Estacionario ---
# La temperatura en una ciudad.
# La media de temperatura en Enero es muy diferente
# a la media de temperatura en Julio.
#
# Como la media cambia con el tiempo (depende de la
# estación), el proceso "Temperatura" no es estacionario.

print("\nProceso NO Estacionario (Ej: Temperatura de una ciudad)")
media_temp_enero = 15.0
media_temp_julio = 28.0
print(f"  Media en Enero (t=1): {media_temp_enero}")
print(f"  Media en Julio (t=7): {media_temp_julio} (La media cambia)")