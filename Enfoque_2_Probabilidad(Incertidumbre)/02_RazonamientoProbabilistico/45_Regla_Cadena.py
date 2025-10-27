# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #45
# "Regla de la Cadena (Probabilidad)"

# La Regla de la Cadena nos permite calcular la
# "Probabilidad Conjunta Completa" (la prob. de que *todo*
# en el modelo ocurra de una forma específica) usando
# probabilidades condicionales.
#
# Fórmula General:
# P(A, B, C) = P(A) * P(B | A) * P(C | A, B)
#
# ...pero en una Red Bayesiana, usamos la "Independencia Condicional"
# para simplificar esto enormemente.
#
# P(Variable) = P(Variable | Padres(Variable))
#
# Fórmula de la Regla de la Cadena *para una Red Bayesiana*:
#
# P(X1, X2, ..., Xn) = PRODUCTO [ P(Xi | Padres(Xi)) ]
#                      (para i=1 hasta n)

# --- Ejemplo: Red de Alarma (del Algoritmo 44) ---
#
# Variables: R, T, A, J, M
#
# Padres(R) = {}
# Padres(T) = {}
# Padres(A) = {R, T}
# Padres(J) = {A}
# Padres(M) = {A}
#
# Pregunta: ¿Cuál es la prob. de un escenario específico?
# P(R=v, T=f, A=v, J=v, M=f) = ?

# Aplicando la Regla de la Cadena Bayesiana:
# P(R, T, A, J, M) = P(R) * P(T) * P(A|R,T) * P(J|A) * P(M|A)

print("Regla de la Cadena (para Redes Bayesianas)")
print("Nos permite calcular la probabilidad conjunta completa")
print("multiplicando las CPTs de la red.")
print("\nP(X1, ..., Xn) = Producto [ P(Xi | Padres(Xi)) ]")
print("\nEjemplo de Alarma:")
print("P(R, T, A, J, M) = P(R) * P(T) * P(A|R,T) * P(J|A) * P(M|A)")
print("\nPara calcular P(Robo=T, Terremoto=F, Alarma=T, Juan=T, Maria=F):")
print("= P(R=T) * P(T=F) * P(A=T|R=T,T=F) * P(J=T|A=T) * P(M=F|A=T)")
print("(Solo buscaríamos esos 5 valores en las CPTs y los multiplicaríamos)")