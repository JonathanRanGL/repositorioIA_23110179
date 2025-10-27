# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #61
# "Naïve-Bayes"

# Es un clasificador probabilístico basado en la Regla de Bayes
# con una suposición "ingenua" (naïve).
#
# Suposición "Naïve": Todas las "características" (features)
# son condicionalmente independientes, dada la clase.
#
# P(Clase | F1, F2) = alfa * P(Clase) * P(F1 | Clase) * P(F2 | Clase)
#
# En lugar de P(F1, F2 | Clase), solo multiplicamos
# P(F1 | Clase) y P(F2 | Clase). Esto lo hace muy rápido.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. Cargar datos (features=largo/ancho de pétalo/sépalo, target=especie)
X, y = load_iris(return_X_y=True)
print("Clasificador Naïve-Bayes (con Scikit-Learn)")
print(f"Forma de los datos X (features): {X.shape}")
print(f"Forma de las etiquetas y (clases): {y.shape}")

# 2. Separar en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Inicializar el clasificador
# (Gaussiano asume que las features continuas siguen una dist. normal)
model = GaussianNB()

# 4. Entrenar el modelo
# (Calcula P(Clase) y P(Feature | Clase) de los datos de ent.)
print("\nEntrenando el modelo...")
model.fit(X_train, y_train)

# 5. Hacer predicciones
print("Haciendo predicciones en datos de prueba...")
y_pred = model.predict(X_test)

# 6. Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPredicciones (primeros 5): {y_pred[:5]}")
print(f"Reales (primeros 5):       {y_test[:5]}")
print(f"\nPrecisión (Accuracy): {accuracy * 100:.2f}%")