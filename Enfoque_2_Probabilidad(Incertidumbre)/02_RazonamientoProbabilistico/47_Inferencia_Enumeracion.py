# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #47
# "Inferencia por Enumeración"

# Es el algoritmo más simple (y más lento) para hacer
# inferencia (preguntas) en una Red Bayesiana.
#
# Pregunta: P(X | e)
#   X = Variable de consulta (Query)
#   e = Evidencia (lo que sabemos)
#
# Fórmula: P(X | e) = alfa * SUMA( P(X, e, y) )
#            (sobre todas las variables ocultas 'y')
#
# P(X, e, y) se calcula usando la Regla de la Cadena.

# --- Ejemplo: Red Simple (Lluvia -> Mojado) ---
#
# Variables: Lluvia (L), Mojado (M)
# P(L) = {T: 0.3, F: 0.7} (Prior)
#
# CPT de P(M | L):
# L=T -> P(M=T)=0.9, P(M=F)=0.1
# L=F -> P(M=T)=0.2, P(M=F)=0.8
#
# Pregunta: ¿Cuál es P(L | M=T)?
# (Prob. de que esté lloviendo, *dado que* el pasto está mojado)
#
# X = L
# e = M=T
# y = {} (No hay variables ocultas)
#
# P(L | M=T) = alfa * P(L, M=T)
#
# P(L, M=T) es una distribución (un vector):
#   - P(L=T, M=T) = P(L=T) * P(M=T | L=T) = 0.3 * 0.9 = 0.27
#   - P(L=F, M=T) = P(L=F) * P(M=T | L=F) = 0.7 * 0.2 = 0.14
#
# Vector (sin normalizar) = <0.27, 0.14>

print("Inferencia por Enumeración")
print("Calcula P(X|e) sumando sobre todas las variables ocultas.")
print("\nEjemplo: P(Lluvia | Mojado=T)")
print("P(L | M=T) = alfa * P(L, M=T)")

# Vector P(L, M=T)
P_L_y_M_T = {
    'L=T': 0.3 * 0.9, # P(L=T) * P(M=T|L=T)
    'L=F': 0.7 * 0.2  # P(L=F) * P(M=T|L=F)
}
print(f"\nVector P(L, M=T) (sin normalizar): {P_L_y_M_T}")

# Normalización (alfa)
suma_total = sum(P_L_y_M_T.values())
alfa = 1.0 / suma_total
print(f"Suma (Evidencia P(M=T)): {suma_total}")

P_L_dado_M_T = {
    'L=T': P_L_y_M_T['L=T'] * alfa,
    'L=F': P_L_y_M_T['L=F'] * alfa
}

print(f"\nVector P(L | M=T) (normalizado):")
print(f"  P(L=T | M=T) = {P_L_dado_M_T['L=T']:.4f}")
print(f"  P(L=F | M=T) = {P_L_dado_M_T['L=F']:.4f}")