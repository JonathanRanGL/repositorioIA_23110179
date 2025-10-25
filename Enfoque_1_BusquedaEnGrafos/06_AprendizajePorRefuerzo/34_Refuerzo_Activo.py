# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #34
# "Aprendizaje por Refuerzo Activo (Concepto)"

# Agente Activo: El agente *no* tiene una política fija.
# Su objetivo es aprender la política *óptima* pi(s)
# mientras explora el entorno.
#
# Para hacer esto, debe aprender la utilidad de las *acciones*.
# Esto es Q-Learning (el siguiente algoritmo).
#
# Un agente activo debe balancear:
# 1. Explotación: Tomar la acción que *cree* que es la mejor.
# 2. Exploración: Tomar una acción aleatoria para *descubrir*
#    si hay acciones mejores que aún no conoce.
#
# Este archivo es conceptual. El Algoritmo #35 (Q-Learning)
# es la implementación de un agente activo.

print("Aprendizaje por Refuerzo Activo (Conceptual)")
print("El agente aprende la política óptima explorando el mundo.")
print("\nComponentes clave:")
print("1. Función Q(s, a): La 'Calidad' o 'Utilidad' de tomar")
print("   la acción 'a' en el estado 's'.")
print("   (Esto es lo que el Agente Q-Learning aprende).")
print("\n2. Política derivada de Q:")
print("   - Explotación: pi(s) = argmax_a Q(s, a)")
print("     (Elegir la 'a' con el mejor valor Q en el estado 's')")
print("   - Exploración: (ej. Epsilon-Greedy)")
print("     'Con probabilidad Epsilon, tomar una acción aleatoria.'")
print("     'Si no, tomar la mejor acción (explotar)'.")
print("\nVer '35_Q_Learning.py' para la implementación.")

# Ejemplo de decisión Epsilon-Greedy (conceptual)
# Q_s = {'Izq': 10, 'Der': 20}
# epsilon = 0.1
#
# if random.random() < epsilon:
#     accion = random.choice(['Izq', 'Der']) # Explorar
# else:
#     accion = 'Der' # Explotar (la de mayor Q-value)