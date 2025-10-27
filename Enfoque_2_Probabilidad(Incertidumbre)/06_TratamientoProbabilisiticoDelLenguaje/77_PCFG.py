# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #77
# "Gramáticas Probab. Independ. del Contexto (PCFG)"

# Una "Gramática Independiente del Contexto" (CFG) define
# las reglas sintácticas de un lenguaje.
#
# S -> NP VP  (Una Oración (S) es un Sintagma Nominal (NP)
#              seguido de un Sintagma Verbal (VP))
# NP -> Det N (Un NP es un Determinante (Det) y un Nombre (N))
# Det -> "el"
# N -> "gato"

# Una "PCFG" añade *probabilidades* a esas reglas.
#
# Si hay dos reglas para NP:
# 1. NP -> Det N
# 2. NP -> N
#
# Una PCFG les asigna probabilidades:
# P(NP -> Det N) = 0.8
# P(NP -> N)   = 0.2
# (La suma de probabilidades para un mismo símbolo
#  de la izquierda (NP) debe ser 1).
#
# Esto permite resolver la "ambigüedad" del lenguaje.
# Si una oración tiene dos árboles sintácticos (parses) posibles,
# la PCFG nos dice cuál es el más probable (multiplicando
# las probabilidades de todas las reglas usadas).

print("Gramática Probabilística Indep. del Contexto (PCFG)")
print("Asigna probabilidades a las reglas sintácticas.")
print("\nEjemplo de Reglas para Sintagma Nominal (NP):")
print("  P(NP -> Det N) = 0.8")
print("  P(NP -> N)     = 0.2")
print("  --------------------")
print("  Suma           = 1.0")

print("\nEjemplo de Reglas para Verbo (V):")
print("  P(V -> 'come') = 0.7")
print("  P(V -> 'duerme') = 0.3")

print("\nSe usa para 'Parsing Probabilístico':")
print("Dada una oración, encontrar el árbol sintáctico")
print("más probable (ej. Algoritmo CYK Probabilístico).")