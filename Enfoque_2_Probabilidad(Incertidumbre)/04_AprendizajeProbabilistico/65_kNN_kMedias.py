# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #65
# "k-NN, k-Medias y Clustering"

# Este ítem combina dos algoritmos muy diferentes.
# k-Medias (k-Means) -> Clustering (No Supervisado)
# k-NN (k-Nearest Neighbors) -> Clasificación (Supervisado)

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Cargar datos
X, y = load_iris(return_X_y=True)

# --- 1. k-Medias (k-Means) (Clustering No Supervisado) ---
# Objetivo: Agrupar los datos X en k grupos.
print("--- 1. k-Medias (k-Means) (No Supervisado) ---")
k = 3 # Sabemos que hay 3 especies
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)

# Entrenamos (solo con X, sin 'y')
kmeans.fit(X)

# Obtenemos los centroides (medias) aprendidos
centroides = kmeans.cluster_centers_
# Obtenemos las etiquetas de clúster asignadas
grupos_asignados = kmeans.labels_

print(f"Centroides (medias) encontrados para {k} grupos:")
print(centroides.round(2))
print(f"\nGrupos asignados (primeros 15): {grupos_asignados[:15]}")
print(f"Etiquetas reales (primeros 15): {y[:15]}")
print("(Nota: k-Means funciona bien, 'Grupo 1' corresponde a 'Real 0')")


# --- 2. k-NN (k-Nearest Neighbors) (Clasificación Supervisada) ---
# Objetivo: Predecir la etiqueta 'y' de un dato nuevo,
# mirando las 'k' etiquetas de sus vecinos más cercanos.
print("\n\n--- 2. k-NN (k-Vecinos Cercanos) (Supervisado) ---")

# Separamos datos (esta vez sí usamos 'y')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k_vecinos = 5
knn = KNeighborsClassifier(n_neighbors=k_vecinos)

# "Entrenar" (Realmente solo memoriza los datos)
print(f"Entrenando k-NN con k={k_vecinos}...")
knn.fit(X_train, y_train)

# Predecir
y_pred = knn.predict(X_test)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión de k-NN: {accuracy * 100:.2f}%")