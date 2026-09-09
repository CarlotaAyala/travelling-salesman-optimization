# 🧬 Travelling Salesman Problem Optimization with Genetic Algorithms

Optimization of the **Travelling Salesman Problem (TSP)** using a **Genetic Algorithm** implemented in Python.

The goal of the project is to find a short route that visits every city exactly once and returns to the starting point. The implementation explores different evolutionary strategies and studies how changes in selection, crossover, mutation, elitism and algorithm parameters affect the quality of the final solution.

---

## 🎯 Project Overview

The Travelling Salesman Problem is a classic combinatorial optimization problem: given a set of cities and the distance between them, the objective is to find the shortest possible closed route that visits each city exactly once.

In this project, candidate routes are treated as individuals in a population and evolved through several generations using a Genetic Algorithm.

The project progressively develops and improves the algorithm across several Python scripts.

---

## 🧠 Genetic Algorithm

The main evolutionary process follows these steps:

1. Generate an initial population of random routes.
2. Calculate the total distance of every route.
3. Select promising individuals as parents.
4. Apply crossover to generate new valid routes.
5. Apply mutation to introduce diversity.
6. Replace the population with the new generation.
7. Repeat the process for a fixed number of generations.
8. Return the shortest route found.

Because the objective is minimization, routes with a lower total distance represent better solutions.

---

## 🧬 Evolutionary Operators

### Selection

Different versions of the project use **tournament selection** to choose parents.

A small group of candidate routes is sampled from the population and the route with the lowest distance is selected.

### Crossover

The project uses order-preserving crossover strategies designed for permutation-based problems such as TSP.

A segment from one parent is preserved while the remaining cities are filled using the order in which they appear in the second parent.

This ensures that every city appears exactly once in the offspring.

### Mutation

Different mutation strategies are explored throughout the project:

- **Swap mutation:** exchanges the positions of two cities.
- **Inversion mutation:** reverses a randomly selected segment of the route.

Mutation introduces diversity into the population and helps reduce the risk of premature convergence.

### Elitism

One version of the algorithm preserves part of the best-performing population directly in the next generation.

This prevents high-quality solutions from being lost during crossover and mutation.

---

## 📂 Project Files

### `Código0.py`

Initial implementation of the Genetic Algorithm using a small five-city example.

It introduces the main components of the solution:

- Distance matrix calculation.
- Random route generation.
- Route evaluation.
- Tournament selection.
- Order crossover.
- Swap mutation.
- Evolution over multiple generations.

### `Código1.py`

Extends the algorithm to the complete TSP dataset.

It:

- Loads the city coordinates from the provided data file.
- Reads a reference solution.
- Executes the Genetic Algorithm on the full problem.
- Compares the distance obtained by the algorithm with the reference route.

### `Código2.py`

Introduces modifications intended to improve the search process, including:

- Larger population size.
- More generations.
- Tournament selection.
- Elitism.
- Inversion mutation.

This version explores a stronger balance between **exploration and exploitation**.

### `Código3.py`

Adds experimental analysis of the Genetic Algorithm.

It compares different **mutation rates** across repeated executions and visualizes the resulting route distances using boxplots.

This makes it possible to study how parameter selection affects the stability and quality of the solutions.

---

## 📊 Mutation Rate Experiment

The final version evaluates several mutation rates through repeated executions of the Genetic Algorithm.

For every mutation rate:

1. The algorithm is executed multiple times.
2. The best route distance from each execution is stored.
3. The distributions of the obtained distances are compared.
4. A boxplot is generated to visualize the effect of mutation rate on solution quality.

This experiment illustrates an important concept in evolutionary computation: the balance between **exploration and exploitation**.

A mutation rate that is too low may reduce population diversity, while an excessively high mutation rate can disrupt good solutions.

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)

### Main libraries

- `numpy`
- `random`
- `matplotlib`

---

## 📂 Repository Structure

```text
travelling-salesman-optimization/
│
├── Código0.py
├── Código1.py
├── Código2.py
├── Código3.py
├── data_TSP_cities_Ejercicio_Práctico_MÓDULO_2_v20250318.dat
├── Ruta Solución
├── Ejercicio_Práctico_MÓDULO_2_v20250318.pdf
└── README.md
```

> **Important:** `Código1.py`, `Código2.py` and `Código3.py` read the file `Ruta Solución` to compare the Genetic Algorithm with the provided reference route. Keep this file in the same directory as the scripts.

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/CarlotaAyala/travelling-salesman-optimization.git
```

2. Enter the project directory:

```bash
cd travelling-salesman-optimization
```

3. Install the required libraries:

```bash
pip install numpy matplotlib
```

4. Run one of the implementations, for example:

```bash
python Código3.py
```

Make sure the city dataset and `Ruta Solución` file are located in the same directory as the Python scripts.

---

## 💡 What I Learned

This project helped me understand how evolutionary algorithms can be applied to complex combinatorial optimization problems.

In particular, I worked with:

- Representation of solutions as permutations.
- Fitness evaluation through route distance.
- Tournament selection.
- Order-based crossover.
- Swap and inversion mutation.
- Elitism.
- Population-based search.
- Exploration vs. exploitation.
- Genetic Algorithm parameter tuning.
- Repeated experiments and comparison of stochastic results.

The project also illustrates why stochastic optimization algorithms should be evaluated across multiple executions rather than relying on the result of a single run.

---

## 🎓 Academic Context

This project was developed as part of the **Artificial Intelligence for Data Science (IACD)** course in the **Data Science and Engineering** degree at the **University of Las Palmas de Gran Canaria (ULPGC)**.

---

## 👩‍💻 Author

**Carlota Ayala**

Data Science and Engineering student  
University of Las Palmas de Gran Canaria (ULPGC)
