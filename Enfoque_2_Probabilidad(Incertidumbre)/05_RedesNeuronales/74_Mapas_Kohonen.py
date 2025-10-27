# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #74
# "Mapas Autoorganizados de Kohonen (SOM)"

# Un SOM es un tipo de Red Neuronal *No Supervisada*.
# (Como k-Means, Algoritmo #65).
#
# Su objetivo es hacer "Reducción de Dimensionalidad" y "Clustering"
# al mismo tiempo.
#
# Toma datos de alta dimensión (ej. 100 features) y
# los "mapea" a una cuadrícula de 2D (o 1D),
# preservando la "topología" de los datos.
#
# "Preservar Topología" = Datos que eran cercanos en
# el espacio de 100D, terminarán siendo cercanos
# en la cuadrícula 2D.

# --- Cómo Funciona (Conceptual) ---
#
# 1. Cuadrícula (Grid): Se crea una cuadrícula de neuronas
#    (ej. 10x10). Cada neurona tiene un vector de "pesos"
#    de la misma dimensión que los datos de entrada (100).
#
# 2. Bucle de Entrenamiento:
#
#    a. Muestreo: Se toma un dato (X) de entrada.
#
#    b. Búsqueda: Se encuentra la "Unidad Mejor Coincidente" (BMU).
#       (La neurona de la cuadrícula cuyo vector de pesos
#        es *más similar* al dato X).
#
#    c. Actualización: Se "tira" del vector de pesos de la BMU
#       para que se parezca *aún más* al dato X.
#
#    d. Cooperación: (Lo más importante) También se "tira"
#       de los *vecinos* de la BMU en la cuadrícula 2D,
#       pero con menos fuerza.
#
# 3. Resultado:
#    La cuadrícula 2D se "pliega" y "organiza" para
#    reflejar la estructura de los datos de 100D.
#    Clústeres en los datos de entrada se volverán
#    "regiones" en el mapa 2D.

print("Mapas Autoorganizados de Kohonen (SOM)")
print("Red Neuronal No Supervisada para clustering y")
print("reducción de dimensionalidad (visualización).")
print("\nObjetivo: Mapear datos N-D a una cuadrícula 2D,")
print("preservando la topología (vecindad).")
print("\nProceso:")
print("1. Se toma un dato X.")
print("2. Se encuentra la neurona 'BMU' (la más similar) en la cuadrícula 2D.")
print("3. Se actualiza la BMU para que se parezca más a X.")
print("4. Se actualizan los *vecinos* de la BMU (con menos fuerza).")
print("\n(Requiere bibliotecas especializadas como 'MiniSom')")