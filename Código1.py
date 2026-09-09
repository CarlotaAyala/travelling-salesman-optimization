import numpy as np
import random

# Cargar coordenadas de las 48 ciudades desde el archivo proporcionado
coordenadas_path = "data_TSP_cities_Ejercicio_Práctico_MÓDULO_2_v20250318.dat"
ruta_solucion_path = "Ruta Solución"

# Leer coordenadas de las ciudades
ciudades = []

with open(coordenadas_path, "r") as f:
    for linea in f:
        partes = linea.strip().split()
        try:
            x, y = float(partes[1]), float(partes[2])
            ciudades.append([x, y])
        except (ValueError, IndexError):
            continue

CITIES = np.array(ciudades)

# Leer la ruta solución
ruta_solucion = []

with open(ruta_solucion_path, "r") as f:
    for linea in f:
        for x in linea.strip().split():
            try:
                ruta_solucion.append(int(x))
            except ValueError:
                continue

# Convertir ruta solución a base 0 si está en base 1
if max(ruta_solucion) == 48:
    ruta_solucion = [i - 1 for i in ruta_solucion]

# Eliminar el último duplicado si es necesario (cuando cierra el ciclo)
if ruta_solucion[-1] == ruta_solucion[0]:
    ruta_solucion = ruta_solucion[:-1]

# Función para calcular la distancia entre ciudades
def calculate_distance(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i_ in range(num_cities):
        for j_ in range(num_cities):
            distance_matrix[i_, j_] = np.linalg.norm(cities[i_] - cities[j_])
    return distance_matrix

# Función para calcular la distancia total de una ruta
def calculate_route_distance(route, distance_matrix):
    distance = 0.0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i], route[i + 1]]
    distance += distance_matrix[route[-1], route[0]]  # Regreso al inicio
    return distance

# Función para crear una ruta aleatoria
def create_route(number_cities):
    return np.random.permutation(number_cities)

# Función de cruce (crossover)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start: end] = parent1[start: end]
    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

# Función de mutación
def mutate(child, mutation_rate):
    for swapped in range(len(child)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(child))
            city1, city2 = child[swapped], child[swap_with]
            child[swapped], child[swap_with] = city1, city2
    return child

def TSP_genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.01):
    distance_matrix = calculate_distance(cities)
    population = [create_route(len(cities)) for _ in range(population_size)]
    for generation in range(generations):
        population = sorted(population, key=lambda route: calculate_route_distance(route, distance_matrix))
        next_generation = population[: population_size // 2]
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(next_generation, 2)
            child = crossover(parent1, parent2)
            next_generation.append(mutate(child, mutation_rate))
        population = next_generation
    best_route = population[0]
    return best_route, calculate_route_distance(best_route, distance_matrix)

# Ejecución y comparación con la ruta solución
distance_matrix = calculate_distance(CITIES)
distancia_ruta_solucion = calculate_route_distance(ruta_solucion, distance_matrix)

# Ejecutar el algoritmo genético
best_route, best_distance = TSP_genetic_algorithm(CITIES)

print("Mejor ruta encontrada:", best_route)
print("Distancia de la mejor ruta encontrada:", best_distance)
print("Distancia de la ruta solución:", distancia_ruta_solucion)

