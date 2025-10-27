# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #78
# "Gramáticas Probabilísticas Lexicalizadas"

# Es una mejora sobre las PCFG (Algoritmo #77).
#
# Problema de las PCFG:
# NP -> V NP
# (Ej. "romper la ventana")
# NP -> P NP
# (Ej. "el hombre con el sombrero")
#
# Una PCFG trata ambas reglas de NP como iguales.
# Pero semánticamente, "romper" (un verbo) es muy
# diferente de "con" (una preposición).
#
# "Lexicalizar" significa hacer que las reglas
# dependan de una "palabra principal" (head).
#
# PCFG:
#   P(NP -> V NP)
#
# PCFG Lexicalizada:
#   P(NP(cabeza_NP) -> V(cabeza_V) NP(cabeza_NP2) | cabeza_V)
#
# Ejemplo:
# La regla "VP -> V NP" ahora depende de la palabra (lexema)
# del verbo (V).
#
# P(VP -> V NP | V='comió')
# (La prob. de expandir un VP con un V y un NP,
#  dado que el verbo es "comió")
#
# P(VP -> V NP | V='durmió')
#
# El modelo aprenderá que P(VP -> V NP | 'comió') es alta
# (porque "comió" suele llevar objeto directo: "comió manzanas").
#
# Y aprenderá que P(VP -> V NP | 'durmió') es muy baja
# (porque "durmió" no suele llevar objeto: "durmió la cama" es raro).
#
# Esto hace que los analizadores (parsers) sean
# mucho más precisos (ej. Collins Parser, Charniak Parser).

print("Gramáticas Probabilísticas Lexicalizadas (Lexicalized PCFG)")
print("Mejora las PCFG al hacer que las probabilidades de las")
print("reglas dependan de la 'palabra principal' (head) de la regla.")
print("\nEjemplo:")
print("  PCFG: P(VP -> V NP)")
print("  Lexicalizada: P(VP -> V NP | V='comió')")
print("  Lexicalizada: P(VP -> V NP | V='durmió')")
print("\nEl modelo aprende que 'comió' toma un NP (objeto),")
print("pero 'durmió' usualmente no, mejorando la precisión")
print("al resolver ambigüedades.")