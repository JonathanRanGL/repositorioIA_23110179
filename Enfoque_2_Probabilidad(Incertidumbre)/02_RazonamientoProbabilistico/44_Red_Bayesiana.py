# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #44
# "Red Bayesiana (Concepto)"

# Una Red Bayesiana (o Red de Creencia) es un modelo gráfico
# para representar la incertidumbre.
# Es un Grafo Dirigido Acíclico (DAG).

# Tiene dos componentes:
# 1. Nodos: Representan las variables aleatorias (ej. Clima, Dolor).
# 2. Arcos (Flechas): Representan la influencia causal/probabilística.
#    (ej. Lluvia -> Mojado). Una flecha de A a B significa
#    que A es un "padre" de B.

# La flecha almacena la "Probabilidad Condicionada" P(B | A).

# --- Ejemplo: Sistema de Alarma de Casa ---
#
# Variables:
# - Robo (R)
# - Terremoto (T)
# - Alarma (A)
# - Juan Llama (J)
# - María Llama (M)
#
# Estructura del Grafo:
#
#    (R)     (T)
#      \       /
#       v     v
#       (Alarma)
#         /   \
#        v     v
#      (J)     (M)
#
# - Un Robo (R) o un Terremoto (T) pueden activar la Alarma (A).
# - La Alarma (A) puede causar que Juan (J) o María (M) llamen.

# Cada nodo tiene una Tabla de Probabilidad Condicional (CPT):
# - P(R) ... (Prior)
# - P(T) ... (Prior)
# - P(A | R, T) ... (CPT de Alarma, depende de sus padres)
# - P(J | A) ... (CPT de Juan, depende de Alarma)
# - P(M | A) ... (CPT de María, depende de Alarma)

print("Red Bayesiana (Concepto)")
print("Es un grafo (DAG) que representa dependencias")
print("probabilísticas entre variables.")
print("\nEjemplo de Grafo:")
print("  (Robo) -> (Alarma) <- (Terremoto)")
print("  (Alarma) -> (Juan Llama)")
print("  (Alarma) -> (María Llama)")
print("\nCada nodo almacena una Tabla de Probabilidad Condicional (CPT)")
print("Ej. P(Alarma | Robo, Terremoto)")