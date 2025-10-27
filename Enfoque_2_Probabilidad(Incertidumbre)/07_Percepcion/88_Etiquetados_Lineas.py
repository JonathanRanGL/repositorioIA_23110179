# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #88
# "Etiquetados de Líneas (Waltz Algorithm)"

# Es un algoritmo clásico de "Visión 3D" para
# interpretar dibujos "lineales" (line-art) de
# objetos poliédricos (bloques, cubos).
#
# Objetivo: Determinar si el dibujo 2D es una
# representación *válida* de un objeto 3D.
#
# Lo hace asignando "etiquetas" a cada línea,
# basado en el tipo de "vértice" (unión) donde se juntan.
#
# --- 1. Etiquetas de Líneas ---
# Cada línea debe ser una de tres cosas:
#
#  + (Convexa): Un borde "apuntando hacia ti".
#  - (Cóncava): Un borde "alejándose de ti" (una esquina interna).
#  > (Oclusiva): El contorno del objeto, donde la cara
#               frontal tapa a la trasera. (La flecha
#               apunta dejando la cara visible a la derecha).

print("Etiquetado de Líneas (Algoritmo de Waltz)")
print("Interpreta dibujos 2D de objetos 3D (poliédricos).")
print("\n1. Etiquetas de Líneas:")
print("  + : Borde Convexo (hacia ti)")
print("  - : Borde Cóncavo (lejos de ti)")
print("  > : Borde Oclusivo (contorno)")

# --- 2. Catálogo de Vértices ---
#
# El algoritmo tiene un "catálogo" de todos los
# vértices 3D físicamente *posibles*.
# (Ej. Vértice 'L', Vértice 'T', Vértice 'Flecha', Vértice 'Y')
#
# Para un Vértice 'Y' (como la esquina de un cubo),
# solo hay 1 etiquetado válido:
#
#     +
#      \
#       Y --- +
#      /
#     +
#
# (Las 3 líneas deben ser convexas).
#
# --- 3. Propagación de Restricciones ---
#
# Es un algoritmo de CSP (Algoritmo #17).
# 1. Empieza en un vértice y asigna una etiqueta válida.
# 2. "Propaga" esa restricción al vértice vecino
#    (ya que la línea que los conecta debe tener la
#     misma etiqueta en ambos extremos).
# 3. Si en algún punto un vértice no tiene ninguna
#    etiqueta válida en el catálogo que coincida
#    con las restricciones de sus vecinos, el
#    algoritmo falla.
#
# Resultado: Si encuentra un etiquetado completo,
# el objeto es (probablemente) 3D válido.

print("\n2. Algoritmo (Propagación de Restricciones):")
print("  - Se usa un 'catálogo' de vértices 3D válidos.")
print("  - Se propagan las etiquetas (+, -, >) de vértice a vértice.")
print("  - Si se encuentra una contradicción, el objeto es 'imposible'.")