# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #76
# "Modelo Probabilístico del Lenguaje: Corpus"

# Un "Corpus" es una gran colección de texto (ej. todos
# los artículos de Wikipedia, millones de tuits).
# Es el conjunto de datos que usamos para "entrenar".
#
# Un "Modelo Probabilístico del Lenguaje" (LM) aprende
# la probabilidad de una secuencia de palabras: P(W).
#
# P("hola mundo") vs P("hola mantis")
#
# El modelo más simple es el "n-grama".
# Un n-grama es una secuencia de N palabras.
# - Bigrama (2-grama): ("hola", "mundo")
# - Trigrama (3-grama): ("nos", "vemos", "mañana")
#
# El modelo aprende P(palabra | palabra_anterior)
# P("mundo" | "hola") = Conteo("hola mundo") / Conteo("hola")

# --- Ejemplo: Entrenamiento de Bigramas ---

# 1. Corpus (Nuestros datos de texto)
corpus = [
    "hola mundo",
    "hola gemini",
    "hola mundo como estas",
    "nos vemos mañana",
    "hola nos vemos"
]

print("Modelo de Lenguaje (Bigramas) entrenado con un Corpus")
print(f"Corpus: {corpus}")

# 2. Tokenizar y contar
conteo_palabras = {} # Conteo("hola")
conteo_bigramas = {} # Conteo("hola mundo")

for oracion in corpus:
    palabras = oracion.split()
    palabras = ["<s>"] + palabras + ["</s>"] # Símbolos de inicio/fin
    
    for i in range(len(palabras) - 1):
        w1 = palabras[i]
        w2 = palabras[i+1]
        
        bigrama = (w1, w2)
        
        # Conteo de palabras individuales (para el denominador)
        conteo_palabras[w1] = conteo_palabras.get(w1, 0) + 1
        # Conteo de bigramas
        conteo_bigramas[bigrama] = conteo_bigramas.get(bigrama, 0) + 1

print(f"\nConteo ('hola'): {conteo_palabras['hola']}")
print(f"Conteo ('hola', 'mundo'): {conteo_bigramas[('hola', 'mundo')]}")

# 3. Calcular Probabilidades (El "Modelo")
# P("mundo" | "hola") = ?
P_mundo_dado_hola = conteo_bigramas[('hola', 'mundo')] / conteo_palabras['hola']

# P("gemini" | "hola") = ?
P_gemini_dado_hola = conteo_bigramas[('hola', 'gemini')] / conteo_palabras['hola']

print("\nModelo Probabilístico (CPT):")
print(f"  P('mundo' | 'hola') = {P_mundo_dado_hola:.2f} (2/4)")
print(f"  P('gemini' | 'hola') = {P_gemini_dado_hola:.2f} (1/4)")