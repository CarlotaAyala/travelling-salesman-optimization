import numpy as np
import random
import matplotlib.pyplot as plt

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
    distance += distance_matrix[route[-1], route[0]]
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

def TSP_genetic_algorithm(cities, population_size=20, generations=200, mutation_rate=0.01):
    distance_matrix = calculate_distance(cities)
    population = [create_route(len(cities)) for _ in range(population_size)]
    best_route = None
    best_distance = float('inf')

    for gen in range(generations):
        fitnesses = [calculate_route_distance(route, distance_matrix) for route in population]
        new_population = []

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

    return best_route, best_distance, distance_matrix

def load_cities_from_file(filepath):
    with open(filepath, 'r') as file:
        cities = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            parts = line.strip().split()
            if len(parts) >= 3:
                x, y = float(parts[1]), float(parts[2])
                cities.append([x, y])
        return np.array(cities)

def load_solution_route(filepath):
    with open(filepath, 'r') as file:
        route = []
        for line in file:
            if line.strip():
                route.append(int(line.strip()) - 1)
        return route

def compare_mutation_effect(cities, mutation_rates=[0.1, 0.001, 0.0003, 0.0002], trials=10):
    results = []
    print("\n=== Comparación de una ejecución individual para cada mutation_rate ===")
    for rate in mutation_rates:
        route, dist, _ = TSP_genetic_algorithm(cities, mutation_rate=rate)
        print(f"Mutation rate: {rate} → Distancia mejor ruta en ejecución individual: {round(dist, 3)}")

        trial_results = []
        for _ in range(trials):
            _, d, _ = TSP_genetic_algorithm(cities, mutation_rate=rate)
            trial_results.append(d)
        results.append(trial_results)

    plt.figure(figsize=(10, 6))
    plt.boxplot(results, labels=[str(r) for r in mutation_rates])
    plt.title("Efecto de la tasa de mutación en la calidad de la solución (distancia)")
    plt.xlabel("Tasa de mutación")
    plt.ylabel("Distancia total del recorrido")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    cities_path = "data_TSP_cities_Ejercicio_Práctico_MÓDULO_2_v20250318.dat"
    solution_path = "Ruta Solución"

    CITIES = load_cities_from_file(cities_path)
    solution_route = load_solution_route(solution_path)

    # Línea base con mutation rate 0.01
    base_route, base_distance, distance_matrix = TSP_genetic_algorithm(CITIES, mutation_rate=0.01)
    solution_distance = calculate_route_distance(solution_route, distance_matrix)

    print("=== Comparación con ruta óptima ===")
    print("Mejor ruta GA (mutation rate 0.01):", base_route[:5], "...", base_route[-5:])
    print("Distancia total GA:", round(base_distance, 3))
    print("Ruta óptima:", solution_route[:5], "...", solution_route[-5:])
    print("Distancia total ruta óptima:", round(solution_distance, 3))

    compare_mutation_effect(CITIES)
