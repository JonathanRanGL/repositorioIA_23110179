# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #73
# "Retropropagación del Error (Backpropagation)"

# Backpropagation es el algoritmo central que permite
# entrenar Redes Neuronales Multicapa (MLPs).
#
# Es cómo la red "aprende" de sus errores.
#
# Funciona en dos fases:

# --- 1. Fase Hacia Adelante (Forward Pass) ---
#    - Se presenta un dato de entrada (X) a la red.
#    - Los datos fluyen a través de las capas:
#      (Entrada) -> (Oculta 1) -> ... -> (Salida)
#    - Se calcula una predicción (y_pred).
#    - Se calcula el "Error" (Loss) comparando la
#      predicción (y_pred) con el valor real (y_true).
#      Error = (y_pred - y_true)^2

print("Retropropagación del Error (Backpropagation)")
print("El algoritmo para entrenar redes multicapa.")
print("\n1. Pase Hacia Adelante (Forward Pass):")
print("   (X) -> [Capa 1] -> [Capa 2] -> (y_pred)")
print("   Se calcula el Error = L(y_pred, y_real)")

# --- 2. Fase Hacia Atrás (Backward Pass) ---
#    - Aquí ocurre la "magia".
#    - Se usa la "Regla de la Cadena" (Cálculo Diferencial)
#      para calcular el "gradiente" del error.
#
#    - Gradiente = ¿Cuánto contribuyó *cada peso (w)*
#                  individual en la red al *error total*?
#
#    - El gradiente se propaga "hacia atrás", desde la
#      capa de salida hasta la capa de entrada.
#
#    - (Gradiente de Salida) -> (Gradiente Oculta 2) -> (Gradiente Oculta 1)
#
# --- 3. Actualización de Pesos ---
#    - Una vez que sabemos el gradiente de cada peso (w),
#      usamos un optimizador (como "Descenso de Gradiente")
#      para *ajustar* el peso en la dirección que
#      *reduzca* el error.
#
#    - w_nuevo = w_viejo - (tasa_aprendizaje * gradiente_w)

print("\n2. Pase Hacia Atrás (Backward Pass):")
print("   Error -> [Capa 2] -> [Capa 1] -> (X)")
print("   Se calcula el Gradiente (derivada del Error")
print("   respecto a cada peso 'w') usando la Regla de la Cadena.")
print("\n3. Actualización de Pesos:")
print("   Se ajustan todos los 'w' para minimizar el Error.")
print("   w = w - (learning_rate * gradiente)")
print("\n(El método 'fit()' del Algoritmo #72 hace todo esto.)")