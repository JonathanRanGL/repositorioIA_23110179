# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #42
# "Independencia Condicional"

# --- Independencia (Simple) ---
# A y B son independientes si saber B no me dice nada sobre A.
# P(A | B) = P(A)
#
# Ejemplo:
# A = "Lanzar moneda 1 = Águila"
# B = "Lanzar moneda 2 = Águila"
# Saber B no cambia mi creencia sobre A.

# --- Independencia Condicional ---
# A y B son condicionalmente independientes *dado C*
# si, una vez que *sabemos* C, B ya no me dice nada nuevo sobre A.
#
# P(A | B, C) = P(A | C)
#
# Esta es la base de las Redes Bayesianas. Permite simplificar
# enormemente los modelos.

# --- Ejemplo: El Dentista ---
#
# Variables:
# C = "Tengo Caries"
# A = "Tengo Dolor de Muela"
# B = "El dentista usa el torno (explorer)"
#
# A (Dolor) y B (Torno) *no* son independientes.
# Si veo que el dentista usa el torno (B), es más probable
# que tenga dolor de muela (A). P(A|B) > P(A)
#
# ...Pero...
#
# Si *ya sabemos* el estado de C (Tengo Caries),
# entonces A y B se vuelven independientes.
#
# Causa Común:
# (Caries) --> (Dolor)
# (Caries) --> (Torno)
#
# Si *ya sé* que tengo Caries (C=True):
# - El dentista usará el torno (B) por la caries.
# - Tendré dolor (A) por la caries.
#
# Ver al dentista usar el torno (B) ya no me da *nueva*
# información sobre mi dolor (A), porque yo ya sabía la causa (C).
#
# P(Dolor | Torno, Caries) = P(Dolor | Caries)

print("Independencia Condicional: P(A | B, C) = P(A | C)")
print("Concepto clave: 'Dado que sé C, B no me da info extra sobre A'")
print("\nEjemplo: Caries (C), Dolor (A), Torno (B)")
print("Dolor y Torno son dependientes.")
print("PERO: Dado que *sé* si tengo Caries (C), el Dolor (A) y")
print("el Torno (B) se vuelven independientes.")
print("La Caries (C) es la 'causa común' que los conecta.")