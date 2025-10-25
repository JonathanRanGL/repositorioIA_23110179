# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #38
# "Incertidumbre (Concepto)"

# La incertidumbre es la incapacidad de saber con certeza
# el estado verdadero del mundo.
#
# Surge por dos razones principales:
# 1. Observabilidad Parcial: Nuestros sensores no ven todo.
#    (Ej. Un doctor no puede "ver" un virus, solo ve los síntomas).
# 2. No Determinismo: El mundo es estocástico.
#    (Ej. Lanzar un dado. Aunque sepa todo, no sé el resultado exacto).
#
# La "Teoría de la Probabilidad" es la herramienta matemática
# que usamos para manejar y razonar *acerca* de la incertidumbre.
#
# En lugar de decir "Tengo gripe", un agente de IA diría:
# P(Gripe) = 0.3   (Hay un 30% de probabilidad de tener gripe)
# P(Alergia) = 0.6 (Hay un 60% de probabilidad de tener alergia)

print("Incertidumbre (Concepto)")
print("La probabilidad nos permite representar y razonar sobre el")
print("conocimiento incompleto o ruidoso del mundo.")

# Ejemplo de creencia bajo incertidumbre:
# ¿Lloverá hoy?
creencia_lluvia = {
    'Llovera': 0.7,
    'No Llovera': 0.3
}

print(f"\nCreencia sobre el clima: {creencia_lluvia}")
print("No estamos 100% seguros, pero podemos tomar decisiones")
print("basadas en estas probabilidades (ej. 70% de llevar paraguas).")