# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #62
# "Algoritmo EM (Expectation-Maximization)"

# Es un algoritmo para encontrar parámetros (ej. medias, varianzas)
# cuando los datos tienen *variables latentes* (ocultas).
#
# Se usa mucho en "clustering" (Agrupamiento), donde la
# "variable latente" es: "¿A qué clúster (grupo) pertenece este dato?"
#
# Funciona en dos pasos iterativos:
# 1. E-Step (Expectation): Estima la variable oculta.
#    (Calcula la *probabilidad* de que cada dato pertenezca a cada clúster).
# 2. M-Step (Maximization): Re-calcula los parámetros del modelo.
#    (Actualiza la 'media' y 'varianza' de cada clúster basado
#     en las probabilidades del E-Step).
#
# Repite hasta que converja.

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
import numpy as np

# 1. Cargar datos (usaremos solo 2 features para simplificar)
iris = load_iris()
X = iris.data[:, :2] # Solo largo y ancho del sépalo
print("Algoritmo EM (usando Gaussian Mixture Model)")
print(f"Datos X (features): {X.shape}")

# 2. Inicializar el modelo
# Queremos encontrar 3 clústeres (K=3), porque sabemos que hay 3 especies
# 'n_init' corre el algoritmo varias veces para evitar malos inicios
gmm = GaussianMixture(n_components=3, n_init=10, random_state=42)

# 3. Entrenar el modelo
# Aquí es donde se ejecutan los pasos E y M iterativamente
print("\nEntrenando el modelo (E-Step, M-Step)...")
gmm.fit(X)

# 4. Resultados (Parámetros aprendidos)
print("\nParámetros aprendidos por EM:")
print("Medias (centroides) de los 3 clústeres:")
print(gmm.means_.round(2))
print("\nCovarianzas (forma) de los 3 clústeres (diagonal):")
print(gmm.covariances_[0].diagonal().round(2))

# 5. Usar el modelo (E-Step final)
# Predecir la probabilidad de que los primeros 2 datos
# pertenezcan a cada uno de los 3 clústeres.
print(f"\nProbabilidades (E-Step) para los primeros 2 datos:")
probs = gmm.predict_proba(X[:2])
print(probs.round(3))
print("(El primer dato pertenece 100% al Clúster 1)")
print("(El segundo dato pertenece 100% al Clúster 0)")