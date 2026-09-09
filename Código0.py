import numpy as np
import random

def calculate_distance(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = np.linalg.norm(cities[i] - cities[j])
    return distance_matrix

def create_route(num_cities):
    return list(np.random.permutation(num_cities))

def calculate_route_distance(route, distance_matrix):
    distance = 0.0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i], route[i + 1]]
    distance += distance_matrix[route[-1], route[0]]  # Regreso a origen
    return distance

def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

def order_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    ptr = end
    for city in parent2:
        if city not in child:
            if ptr >= len(parent1):
                ptr = 0
            child[ptr] = city
            ptr += 1
    return child

def swap_mutation(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def TSP_genetic_algorithm(cities, population_size=50, generations=500, mutation_rate=0.01):
    distance_matrix = calculate_distance(cities)
    population = [create_route(len(cities)) for _ in range(population_size)]
    best_route = None
    best_distance = float('inf')

    for gen in range(generations):
        fitnesses = [calculate_route_distance(route, distance_matrix) for route in population]
        new_population = []

        # Guardar el mejor de la generación
        gen_best_index = np.argmin(fitnesses)
        if fitnesses[gen_best_index] < best_distance:
            best_distance = fitnesses[gen_best_index]
            best_route = population[gen_best_index]

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child = order_crossover(parent1, parent2)
            child = swap_mutation(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return best_route, best_distance

if __name__ == "__main__":
    CITIES = np.array([
        [0, 0], [1, 5], [5, 2], [6, 6], [8, 3]
    ])

    best_route, best_distance = TSP_genetic_algorithm(CITIES)

    print("Mejor recorrido encontrado:", best_route)
    print("Distancia total del recorrido:", round(best_distance, 3))
go sino