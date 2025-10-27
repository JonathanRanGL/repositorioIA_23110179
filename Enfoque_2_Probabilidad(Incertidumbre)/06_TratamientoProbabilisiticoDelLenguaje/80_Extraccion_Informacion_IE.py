# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #80
# "Extracción de Información (Information Extraction - IE)"

# IE es la tarea de "extraer" información estructurada
# (como una base de datos) a partir de texto no estructurado.
#
# (Texto) -> [Algoritmo IE] -> (Base de Datos)

# --- 1. Reconocimiento de Entidades Nombradas (NER) ---
# Tarea: Encontrar y clasificar "entidades" (sustantivos).
#
# Texto: "Apple fue fundada por Steve Jobs en Cupertino en 1976."
#
# NER:
# - "Apple"      -> [ORG] (Organización)
# - "Steve Jobs" -> [PER] (Persona)
# - "Cupertino"  -> [LOC] (Ubicación)
# - "1976"       -> [DATE] (Fecha)
#
# (Esto se aprende usando HMMs, CRFs o Redes Neuronales (LSTMs)).

print("Extracción de Información (IE) - Conceptual")
print("\n--- 1. Reconocimiento de Entidades Nombradas (NER) ---")
print("Texto: 'Apple fue fundada por Steve Jobs en Cupertino.'")
print("Salida NER:")
print("  - 'Apple' -> [ORG]")
print("  - 'Steve Jobs' -> [PER]")
print("  - 'Cupertino' -> [LOC]")

# --- 2. Extracción de Relaciones ---
# Tarea: Encontrar la *relación* entre las entidades.
#
# (Usa la salida de NER)
#
# Entidades: [ORG: Apple], [PER: Steve Jobs]
# Relación: FundadorDe(Entidad1, Entidad2)
#
# Salida: FundadorDe("Steve Jobs", "Apple")
#
# (Se aprende entrenando un clasificador en pares de entidades).

print("\n--- 2. Extracción de Relaciones ---")
print("Usa las entidades de NER para encontrar relaciones.")
print("Salida:")
print("  - Relación: FundadorDe")
print("  - Argumento 1: 'Steve Jobs'")
print("  - Argumento 2: 'Apple'")

print("\n(Se usan bibliotecas como spaCy o NLTK para esto.)")