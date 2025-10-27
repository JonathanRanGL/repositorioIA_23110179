# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #48
# "Eliminación de Variables"

# Es una versión optimizada de la Inferencia por Enumeración.
# Evita cálculos repetidos "empujando" las sumas
# hacia la derecha lo más posible.
#
# P(X | e) = alfa * SUMA_y( P(X, e, y) )
#
# En lugar de sumar al final, suma "factores" intermedios.
#
# --- Ejemplo: Red (Nublado -> Lluvia -> Mojado) ---
# N -> L -> M
# P(N), P(L|N), P(M|L)
#
# Pregunta: P(M) ?  (P(M=T))
#
# P(M) = SUMA_L ( SUMA_N ( P(N) * P(L|N) * P(M|L) ) )
#
# P(M) = SUMA_L ( P(M|L) * ( SUMA_N ( P(N) * P(L|N) ) ) )
#
# 1. "Factor 1" (f1): f1(L) = SUMA_N ( P(N) * P(L|N) )
#    (Eliminamos N, creamos un nuevo factor que solo depende de L)
#
# 2. "Factor 2" (f2): P(M|L) (ya lo tenemos)
#
# 3. Resultado: P(M) = SUMA_L ( f2(M,L) * f1(L) )
#
# Este algoritmo *elimina* N para crear f1(L),
# y luego *elimina* L para crear el resultado P(M).
# Es mucho más eficiente que la enumeración.

print("Eliminación de Variables (Conceptual)")
print("Optimiza la Enumeración al 'empujar' las sumas hacia adentro")
print("y crear 'factores' intermedios.")
print("\nConsulta: P(M) en la red N -> L -> M")
print("P(M) = SUMA_L( SUMA_N( P(N) * P(L|N) * P(M|L) ) )")
print("\nEliminación de Variables lo reordena:")
print("P(M) = SUMA_L( P(M|L) * [ SUMA_N( P(N) * P(L|N) ) ] )")
print("\nPasos:")
print("1. Eliminar N: Calcular f1(L) = SUMA_N( P(N) * P(L|N) )")
print("2. Eliminar L: Calcular P(M) = SUMA_L( P(M|L) * f1(L) )")
print("\nEsto evita recalcular la suma interna de N por cada valor de L.")