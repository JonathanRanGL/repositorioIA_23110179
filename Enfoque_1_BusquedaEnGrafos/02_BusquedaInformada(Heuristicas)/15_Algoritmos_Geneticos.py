# Jonathan Rodrigo Sánchez Rangel   -   23110179   -   6E
# Algoritmo #15
# "Algoritmos Genéticos (GA)"

import random

# Algoritmo Genético: "Optimización inspirada en la evolución".
# 1. Población: Un conjunto de "individuos" (soluciones candidatas).
# 2. Fitness: Qué tan "buena" es una solución.
# 3. Selección: Los mejores individuos (mejor fitness) son elegidos para "reproducirse".
# 4. Crossover: Dos padres "combinan su ADN" (información) para crear un hijo.
# 5. Mutación: Pequeños cambios aleatorios en el ADN del hijo.
# 6. Repetir: La nueva generación reemplaza a la antigua.

# --- Problema de ejemplo ---
# Encontrar una cadena de texto objetivo.
# "Individuo" = una cadena de texto aleatoria (ej. "qx4a!")
# "ADN" = los caracteres
# "Fitness" = cuántos caracteres coinciden con el objetivo
TARGET_STRING = "HOLA"
GENES = " ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Genes posibles

# 1. Función de Fitness
def calculate_fitness(individual):
    fitness = 0
    for i in range(len(TARGET_STRING)):
        if individual[i] == TARGET_STRING[i]:
            fitness += 1
    return fitness

# 2. Función de Crossover
def crossover(parent1, parent2):
    # Crossover de un solo punto
    split_point = random.randint(1, len(TARGET_STRING) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child

# 3. Función de Mutación
def mutate(individual, mutation_rate):
    mutated_individual = ""
    for char in individual:
        if random.random() < mutation_rate:
            # Reemplaza el gen (caracter) por uno aleatorio
            mutated_individual += random.choice(GENES)
        else:
            mutated_individual += char
    return mutated_individual

# --- Configuración del Algoritmo ---
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 200

# 1. Crear Población Inicial
population = []
for _ in range(POPULATION_SIZE):
    individual = "".join(random.choice(GENES) for _ in range(len(TARGET_STRING)))
    population.append(individual)

print(f"Algoritmo Genético (Objetivo: '{TARGET_STRING}')")
print(f"Población inicial (muestra): {population[:5]}")

# --- Bucle de Evolución ---
generation = 0
best_individual = ""
best_fitness = -1

while generation < MAX_GENERATIONS and best_fitness < len(TARGET_STRING):
    
    # Evaluar Fitness de la población
    pop_with_fitness = []
    for individual in population:
        fitness = calculate_fitness(individual)
        pop_with_fitness.append((individual, fitness))
        
        # Guardar el mejor
        if fitness > best_fitness:
            best_fitness = fitness
            best_individual = individual
            print(f"Gen {generation}: Nuevo mejor -> '{best_individual}' (Fitness: {best_fitness})")

    # Si encontramos el objetivo, paramos
    if best_fitness == len(TARGET_STRING):
        break
        
    # 3. Selección (Selección por torneo simple)
    # Ordeno por fitness y me quedo con la mitad superior
    pop_with_fitness.sort(key=lambda x: x[1], reverse=True)
    parents = [ind for ind, fit in pop_with_fitness[:POPULATION_SIZE // 2]]
    
    # 4. Crossover y 5. Mutación
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        # Elijo dos padres aleatorios de la élite
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        
        child = crossover(parent1, parent2)
        mutated_child = mutate(child, MUTATION_RATE)
        
        new_population.append(mutated_child)
        
    # 6. Reemplazo
    population = new_population
    generation += 1
    
print(f"\nEvolución terminada.")
print(f"Mejor solución encontrada: '{best_individual}'")