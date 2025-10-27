# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #66
# "Máquinas de Vectores Soporte (SVM)"

# Una SVM es un clasificador (supervisado) que busca
# encontrar el "hiperplano" (una línea o plano) que
# *mejor* separe las clases en el espacio de features.
#
# "Mejor" significa el hiperplano que maximice el "margen"
# (la distancia a los puntos más cercanos de cada clase).
#
# "Vectores Soporte" son esos puntos que están justo en el margen.
#
# "El Truco del Núcleo (Kernel)":
# Permite a SVMs clasificar datos no-lineales,
# proyectándolos "mágicamente" a una dimensión superior
# donde *sí* son linealmente separables.
# (Kernel 'linear', 'poly', 'rbf')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC # Support Vector Classifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# 1. Cargar datos
X, y = load_iris(return_X_y=True)

# 2. Separar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Escalar datos (Muy importante para SVMs)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Entrenar SVM
print("Máquina de Vectores Soporte (SVM) (con Scikit-Learn)")
print("Entrenando SVM con un Núcleo (Kernel) 'rbf' (no-lineal)...")

# C=1.0 es el parámetro de regularización
# kernel='rbf' (Radial Basis Function) es el más común y potente
model = SVC(kernel='rbf', C=1.0, random_state=42)
model.fit(X_train, y_train)

# 5. Predecir y Evaluar
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPrecisión de SVM (rbf): {accuracy * 100:.2f}%")

# --- Comparación con Kernel Lineal ---
print("\nEntrenando SVM con un Núcleo (Kernel) 'linear'...")
model_linear = SVC(kernel='linear', C=1.0, random_state=42)
model_linear.fit(X_train, y_train)
y_pred_linear = model_linear.predict(X_test)
accuracy_linear = accuracy_score(y_test, y_pred_linear)
print(f"Precisión de SVM (linear): {accuracy_linear * 100:.2f}%")