# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #71
# "Separabilidad Lineal"

# Un problema es "linealmente separable" si existe
# una *línea recta* (en 2D), un *plano* (en 3D) o un
# *hiperplano* (en N-D) que pueda separar
# perfectamente las clases.

# El Perceptrón (Algoritmo #70) solo puede resolver
# problemas linealmente separables.

print("Separabilidad Lineal (Concepto)")

# --- 1. Problemas Linealmente Separables ---
print("\n1. Problemas Linealmente Separables (Resolvibles por Perceptrón):")
print("\n   Función AND:")
print("   X1 | X2 | Y")
print("   ---|---|---")
print("    0 |  0 | 0")
print("    0 |  1 | 0")
print("    1 |  0 | 0")
print("    1 |  1 | 1")
print("   (Se puede trazar una línea que separe los '0' del '1')")

print("\n   Función OR:")
print("   X1 | X2 | Y")
print("   ---|---|---")
print("    0 |  0 | 0")
print("    0 |  1 | 1")
print("    1 |  0 | 1")
print("    1 |  1 | 1")
print("   (También es linealmente separable)")


# --- 2. Problema NO Linealmente Separable ---
print("\n\n2. Problema NO Linealmente Separable (Falla del Perceptrón):")
print("\n   Función XOR (O Exclusivo):")
print("   X1 | X2 | Y")
print("   ---|---|---")
print("    0 |  0 | 0  <- (A)")
print("    0 |  1 | 1  <- (B)")
print("    1 |  0 | 1  <- (B)")
print("    1 |  1 | 0  <- (A)")
print("\n   (Es imposible trazar *una sola línea* que separe")
print("    los puntos 'A' de los 'B'. Se necesitan dos líneas).")
print("\n   Esto requiere una 'Red Multicapa' (Algoritmo #72).")