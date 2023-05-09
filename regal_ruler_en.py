import random

# Fitness function to evaluate a solution
def fitness(solution):
    conflicts = 0
    n = len(solution)

    for i in range(n):
        for j in range(i + 1, n):
            if solution[i] == solution[j]:
                conflicts += 1
            elif abs(solution[i] - solution[j]) == abs(i - j):
                conflicts += 1

    return conflicts

# Crossover operation for the genetic algorithm
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Mutation operation for the genetic algorithm
def mutate(solution):
    index = random.randint(0, len(solution) - 1)
    value = random.randint(1, len(solution))
    mutated_solution = solution[:]
    mutated_solution[index] = value
    return mutated_solution

# RegalRuler function that uses a genetic algorithm to solve the 8-Queens problem
def regal_ruler(population_size, max_generations, mutation_rate):
    n = 8

    # Generate the initial population
    population = [random.sample(range(1, n + 1), n) for _ in range(population_size)]

    for _ in range(max_generations):
        population.sort(key=fitness)

        # Check if a solution is found
        if fitness(population[0]) == 0:
            return population[0]

        # Select the best individuals for crossover
        selected = population[:population_size // 2]

        # Perform crossover and mutation
        new_population = []
        for _ in range(population_size):
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            offspring = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                offspring = mutate(offspring)
            new_population.append(offspring)

        population = new_population

    return None

# Solve the 8-Queens problem using the RegalRuler algorithm
solution = regal_ruler(100, 1000, 0.1)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")