# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #43
# "Regla de Bayes"

# La Regla de Bayes nos permite "invertir" la probabilidad condicional.
#
# Es muy útil para diagnósticos:
# Sabemos P(Síntoma | Enfermedad) -> (Fácil de obtener de estudios)
# Queremos P(Enfermedad | Síntoma) -> (Lo que el doctor necesita)
#
# Fórmula:
#
#             P(B | A) * P(A)
# P(A | B) = -----------------
#                 P(B)
#
# P(Enfermedad | Síntoma) = [ P(Síntoma|Enfermedad) * P(Enfermedad) ] / P(Síntoma)
#
# Posterior = (Verosimilitud * Prior) / Evidencia

# --- Ejemplo: Prueba de Enfermedad Rara ---
#
# P(E) = 0.0001 (Prior: Prob. de tener la enfermedad)
# P(no E) = 0.9999
#
# La prueba (Síntoma 'S') tiene:
# P(S | E) = 0.99 (Sensibilidad: 99% de dar positivo si estás enfermo)
# P(no S | no E) = 0.98 (Especificidad: 98% de dar negativo si estás sano)
#
# ...lo que implica:
# P(no S | E) = 0.01 (Falso negativo)
# P(S | no E) = 0.02 (Falso positivo)
#
# --- Pregunta: Diste positivo (S). ¿Cuál es la prob. de estar enfermo (E)? ---
# P(E | S) = ?

P_E = 0.0001
P_no_E = 0.9999
P_S_dado_E = 0.99
P_S_dado_no_E = 0.02 # Falso positivo

# 1. Calcular el numerador: P(S | E) * P(E)
numerador = P_S_dado_E * P_E
# numerador = 0.99 * 0.0001 = 0.000099

# 2. Calcular el denominador P(S) (Evidencia)
# P(S) = P(S y E) + P(S y no E)
# P(S) = P(S | E) * P(E) + P(S | no E) * P(no E)
P_S = (P_S_dado_E * P_E) + (P_S_dado_no_E * P_no_E)
# P_S = (0.99 * 0.0001) + (0.02 * 0.9999)
# P_S = 0.000099 + 0.019998 = 0.020097

# 3. Calcular el posterior P(E | S)
P_E_dado_S = numerador / P_S

print("Regla de Bayes: P(A|B) = P(B|A) * P(A) / P(B)")
print("\nEjemplo: Prueba de enfermedad")
print(f"P(Enfermo | Positivo) = (P(Positivo|Enfermo) * P(Enfermo)) / P(Positivo)")
print(f"P(E|S) = ({P_S_dado_E} * {P_E}) / {P_S:.6f}")
print(f"P(E|S) = {numerador} / {P_S:.6f}")
print(f"P(E|S) = {P_E_dado_S:.4f}")

print(f"\nAunque diste positivo, la prob. de estar enfermo es solo {P_E_dado_S*100:.2f}%")
print("(Esto es por el alto % de Falsos Positivos (0.02) comparado")
print(" con la baja prob. Priori de la enfermedad (0.0001))")