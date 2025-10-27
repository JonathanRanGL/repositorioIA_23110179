# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #58
# "Red Bayes. Dinámica: Filtrado de Partículas"

# Es un algoritmo de "Filtrado" (como Kalman) pero para
# problemas *no-lineales* y *no-Gaussianos*.
# (Ej. Un robot en un laberinto, donde el sensor es raro).
#
# Es un método de muestreo (aproximado).
# Representa la "creencia" P(X_t) como un conjunto
# de N "partículas" (muestras).
#
# Ciclo: Predecir, Actualizar, Re-muestrear.

import numpy as np
import random

print("Filtrado de Partículas (Simulación 1D No-Lineal)")

# --- 1. Inicialización ---
N_particulas = 1000
# P(X_0): Creencia inicial (distribución normal)
# Partículas = Muestras de la posición inicial
particles = np.random.normal(0.0, 1.0, N_particulas)

# --- 2. Modelos (No Lineales) ---
# Modelo de Transición: x_t = x_t-1 + 1 + ruido
def transition_model(x_t_minus_1):
    return x_t_minus_1 + 1.0 + np.random.normal(0, 0.5) # Ruido de proceso

# Modelo de Observación: p(z | x)
# El sensor es "mejor" cerca de 0 y 5
def observation_model_prob(z_t, x_t):
    # Probabilidad Gaussiana de la observación
    mean = x_t # Sensor mide la posición
    std_dev = 2.0
    prob = (1.0 / (std_dev * np.sqrt(2 * np.pi))) * \
           np.exp(-0.5 * ((z_t - mean) / std_dev)**2)
    return prob

# --- 3. Simulación ---
z_t = 1.2 # Observamos la posición 1.2
print(f"Observación (z_1): {z_t}")

# --- Paso 1: Predecir (Mover las partículas) ---
particles_pred = np.zeros(N_particulas)
for i in range(N_particulas):
    particles_pred[i] = transition_model(particles[i])

# --- Paso 2: Actualizar (Ponderar) ---
# Pesar cada partícula por P(z_t | x_t_particula)
weights = np.zeros(N_particulas)
for i in range(N_particulas):
    weights[i] = observation_model_prob(z_t, particles_pred[i])
    
# Normalizar los pesos
if np.sum(weights) > 0:
    weights = weights / np.sum(weights)
else:
    weights = np.ones(N_particulas) / N_particulas # Si fallan los pesos

# --- Paso 3: Re-muestrear (Resampling) ---
# Elegir N nuevas partículas, seleccionando con
# probabilidad proporcional a 'weights'.
indices = np.random.choice(np.arange(N_particulas), N_particulas, p=weights)
particles_new = particles_pred[indices]

# La nueva "creencia" es la distribución de 'particles_new'
mean_belief = np.mean(particles_new)
std_belief = np.std(particles_new)

print(f"Estimación de P(X_1 | z_1):")
print(f"  Media: {mean_belief:.3f}")
print(f"  StdDev: {std_belief:.3f}")