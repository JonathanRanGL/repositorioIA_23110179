# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #70
# "Perceptrón, ADALINE y MADALINE"

# El Perceptrón (Rosenblatt, 1957) es el modelo de
# neurona artificial más simple.
# Usa la 'step function' (escalón) y aprende
# mediante una regla de aprendizaje simple.
#
# ADALINE (Widrow-Hoff, 1960) es similar, pero
# usa una función de activación lineal y una regla de
# aprendizaje diferente (Delta Rule / Gradient Descent).
#
# MADALINE es "Multiple ADALINEs" (una red multicapa).
#
# Scikit-learn implementa una versión moderna del Perceptrón
# que usa "Stochastic Gradient Descent" (SGD) para entrenar.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 1. Cargar datos (solo 2 clases, 2 features para que sea simple)
iris = load_iris()
# Usamos solo las primeras 100 muestras (clases 0 y 1)
X = iris.data[:100, :2] 
y = iris.target[:100]

print("Perceptrón (con Scikit-Learn)")
print("Clasificando 2 especies de Iris (linealmente separables).")
print(f"Datos X: {X.shape}, Datos y: {y.shape}")

# 2. Escalar datos (importante para SGD)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 3. Separar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Inicializar y Entrenar el Perceptrón
# eta0 = tasa de aprendizaje (learning rate)
# max_iter = cuántas "épocas" (pasadas por los datos)
model = Perceptron(max_iter=100, eta0=0.1, random_state=42)

model.fit(X_train, y_train)

# 5. Evaluar
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nPesos (w) aprendidos: {model.coef_.round(2)}")
print(f"Sesgo (b) aprendido: {model.intercept_.round(2)}")
print(f"\nPrecisión en datos de prueba: {accuracy * 100:.2f}%")
print("(El Perceptrón encontró la línea que separa las clases)")