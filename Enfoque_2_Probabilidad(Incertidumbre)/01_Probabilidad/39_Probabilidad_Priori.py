# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #39
# "Probabilidad a Priori (Prior)"

# La probabilidad a priori, P(A), es la "creencia" que tenemos
# sobre un evento ANTES de tener cualquier evidencia nueva.
# Es la probabilidad base.

# --- Ejemplo: Lanzar un dado ---
#
# P(Dado=1) = 1/6
# P(Dado=2) = 1/6
# ...
# P(Dado=6) = 1/6
#
# Esta es nuestra creencia *a priori* sobre el resultado.

# --- Ejemplo: Diagnóstico Médico ---
#
# Contexto: Un doctor ve a un paciente nuevo.
# Pregunta: ¿Cuál es la prob. de que tenga una enfermedad rara 'E'?
#
# Basado en la población general, el doctor sabe que 1 de cada 10,000
# personas tiene esta enfermedad.
#
# P(E) = 1 / 10000 = 0.0001
# P(no E) = 9999 / 10000 = 0.9999
#
# Esta P(E) es la probabilidad a priori.
# Es la probabilidad que asignamos *antes* de hacer
# cualquier prueba o ver algún síntoma.

print("Probabilidad a Priori (Prior)")

# P(A)
prob_enfermedad_rara = 0.0001
prob_no_enfermedad = 1.0 - prob_enfermedad_rara

print(f"La probabilidad a priori de tener la enfermedad es: {prob_enfermedad_rara}")
print(f"La probabilidad a priori de NO tenerla es: {prob_no_enfermedad}")
print("\nEsta es nuestra creencia base, sin evidencia.")