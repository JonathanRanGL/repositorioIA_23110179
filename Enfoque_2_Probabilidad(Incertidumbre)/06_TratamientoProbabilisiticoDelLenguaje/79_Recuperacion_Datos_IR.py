# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #79
# "Recuperación de Datos (Information Retrieval)"

# IR es el campo de buscar documentos relevantes
# en una gran colección (ej. Google, la biblioteca).
#
# Un modelo clásico es el "Modelo de Espacio Vectorial"
# usando "TF-IDF".

# TF = Term Frequency (Frecuencia del Término)
#    "¿Qué tan importante es la palabra 'IA' en *este* documento?"
#    (Cuántas veces aparece 'IA' en Doc1 / Total de palabras en Doc1)

# IDF = Inverse Document Frequency (Frecuencia Inversa de Documento)
#    "¿Qué tan rara (importante) es la palabra 'IA' en *toda* la colección?"
#    (log(Total de Docs / Docs que contienen 'IA'))
#    (Una palabra como 'el' está en todos los docs, su IDF es 0).

# TF-IDF = TF * IDF
# (Es un 'score' alto si la palabra es frecuente en *este* doc,
#  pero rara en el *resto* de la colección).

from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Corpus (La "colección" de documentos)
corpus = [
    "El perro come croquetas.", # Doc 0
    "El gato come pescado.",    # Doc 1
    "El perro y el gato son mascotas." # Doc 2
]

# 2. Inicializar el modelo TF-IDF
# (Esto tokeniza, cuenta y calcula IDF)
tfidf_vectorizer = TfidfVectorizer()

print("Recuperación de Datos (TF-IDF con Scikit-Learn)")

# 3. Entrenar (Aprender el vocabulario y los IDFs)
#    y Transformar (Calcular los scores TF-IDF)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# 4. Ver resultados
print("\nVocabulario aprendido (Features):")
print(tfidf_vectorizer.get_feature_names_out())

print("\nMatriz TF-IDF (Score por palabra y documento):")
# (Es una matriz dispersa, la convertimos a densa para verla)
print(tfidf_matrix.toarray().round(2))

# 5. Búsqueda (Query)
query = "El gato con croquetas"
print(f"\nQuery: '{query}'")

# Transformamos la query usando el *mismo* modelo
query_vector = tfidf_vectorizer.transform([query])
print("Vector TF-IDF de la Query:")
print(query_vector.toarray().round(2))

# (Un sistema real de IR calcularía la "Similitud Coseno"
#  entre el vector de la query y los vectores de los documentos
#  para encontrar el más relevante).