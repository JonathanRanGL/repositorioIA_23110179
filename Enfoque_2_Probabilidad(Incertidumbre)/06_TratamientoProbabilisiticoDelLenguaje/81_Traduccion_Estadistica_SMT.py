# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #81
# "Traducción Automática Estadística (SMT)"

# SMT fue el enfoque dominante antes de Deep Learning (Redes
# Neuronales Secuencia-a-Secuencia).
#
# Tarea: Traducir de Francés (F) a Inglés (E).
# Queremos encontrar la mejor oración en Inglés (e)
# dada la oración en Francés (f).
#
# P(e | f)
#
# Se usa la Regla de Bayes (Modelo de Canal Ruidoso):
#
# P(e | f) = alfa * P(f | e) * P(e)
#
# 1. P(f | e) = Modelo de Traducción (Alineación)
#    "¿Qué tan probable es que 'la maison' (f) sea la
#     traducción de 'the house' (e)?"
#    - Se aprende de un "corpus paralelo" (textos
#      traducidos, ej. debates de la ONU).
#    - (Ej. IBM Models 1-5).
#
# 2. P(e) = Modelo de Lenguaje (Fluidez)
#    "¿Qué tan probable (fluida) es la oración 'the house'
#     en Inglés?"
#    - (Es un n-grama, Algoritmo #76).
#    - Esto asegura que la traducción suene natural.
#    - P("the house") > P("house the")
#
# El algoritmo de "Decodificación" (Búsqueda) tiene que
# encontrar la oración 'e' que maximice este producto,
# lo cual es un problema de búsqueda muy complejo.

print("Traducción Automática Estadística (SMT)")
print("Traducción (ej. Francés -> Inglés) como un")
print("problema probabilístico (Modelo de Canal Ruidoso).")
print("\nObjetivo: Encontrar 'e' que maximiza P(e | f)")
print("P(e | f) = P(f | e) * P(e)")
print("\n1. P(f | e) = Modelo de Traducción (Alineación)")
print("   (Aprendido de corpus paralelos)")
print("   '¿La frase en F es una buena traducción de la E?'")
print("\n2. P(e) = Modelo de Lenguaje (Fluidez)")
print("   (Aprendido de corpus solo en Inglés)")
print("   '¿La frase en E suena a Inglés natural?'")
print("\n(Hoy en día, SMT ha sido reemplazado por Traducción")
print(" Neuronal (NMT) basada en Transformers).")