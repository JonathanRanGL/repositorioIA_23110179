# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #60
# "Aprendizaje Bayesiano"

# El aprendizaje Bayesiano utiliza la Regla de Bayes
# para *actualizar la creencia* en una hipótesis (H)
# a medida que se observa nueva evidencia (D, de "Datos").

# P(H | D) = alfa * P(D | H) * P(H)
#
# P(H) = "Prior" (Nuestra creencia en la hipótesis *antes* de ver datos)
# P(D | H) = "Verosimilitud" (Qué tan probable es ver esos datos *si* la hipótesis fuera cierta)
# P(H | D) = "Posterior" (Nuestra *nueva* creencia, después de ver los datos)

# --- Ejemplo: La Moneda "Cargada" ---
#
# Hipótesis (H): Tenemos 3 hipótesis sobre una moneda
#   h1: P(Águila) = 0.5 (Justa)
#   h2: P(Águila) = 0.75 (Cargada a Águila)
#   h3: P(Águila) = 0.25 (Cargada a Sol)
#
# Prior P(H): Creemos que todas son igualmente probables
P_H = {'h1': 1/3, 'h2': 1/3, 'h3': 1/3}
print(f"Aprendizaje Bayesiano (Actualización de Creencia)")
print(f"Priors P(H): {P_H}")

# Datos (D): Lanzamos la moneda 3 veces y obtenemos: [Águila, Águila, Sol]
Datos = ['A', 'A', 'S']

# 1. Calcular la Verosimilitud P(D | H) para cada hipótesis
# P(D|h) = P(A|h) * P(A|h) * P(S|h)
P_D_dado_H = {
    'h1': 0.5 * 0.5 * (1 - 0.5), # 0.125
    'h2': 0.75 * 0.75 * (1 - 0.75), # 0.1406
    'h3': 0.25 * 0.25 * (1 - 0.25)  # 0.0468
}
print(f"Verosimilitud P(D|H): {P_D_dado_H}")

# 2. Calcular P(H) * P(D | H) (sin normalizar)
P_H_D_sin_norm = {
    'h1': P_H['h1'] * P_D_dado_H['h1'],
    'h2': P_H['h2'] * P_D_dado_H['h2'],
    'h3': P_H['h3'] * P_D_dado_H['h3']
}

# 3. Normalizar (Calcular alfa)
suma_total = sum(P_H_D_sin_norm.values())
alfa = 1.0 / suma_total

# 4. Calcular Posterior P(H | D)
P_H_dado_D = {h: v * alfa for h, v in P_H_D_sin_norm.items()}

print(f"\nPosterior P(H | D) (Creencia actualizada):")
print(f"  h1 (Justa, 0.5):   {P_H_dado_D['h1']:.4f}")
print(f"  h2 (Cargada A, 0.75): {P_H_dado_D['h2']:.4f} <-- La más probable")
print(f"  h3 (Cargada S, 0.25): {P_H_dado_D['h3']:.4f}")
print("\n(Hemos 'aprendido' que h2 es la más probable)")