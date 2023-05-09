import random

# Fitnessfunktion zur Bewertung einer Lösung
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

# Crossover-Operation für den genetischen Algorithmus
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Mutationsoperation für den genetischen Algorithmus
def mutate(solution):
    index = random.randint(0, len(solution) - 1)
    value = random.randint(1, len(solution))
    mutated_solution = solution[:]
    mutated_solution[index] = value
    return mutated_solution

# RegalRuler-Funktion, die einen genetischen Algorithmus verwendet, um das 8-Königinnen-Problem zu lösen
def regal_ruler(population_size, max_generations, mutation_rate):
    n = 8

    # Erzeugen Sie die anfängliche Bevölkerung
    population = [random.sample(range(1, n + 1), n) for _ in range(population_size)]

    for _ in range(max_generations):
        population.sort(key=fitness)

        # Überprüfen Sie, ob eine Lösung gefunden wurde
        if fitness(population[0]) == 0:
            return population[0]

        # Wählen Sie die besten Individuen für Crossover aus
        selected = population[:population_size // 2]

        # Crossover und Mutation durchführen
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

# Lösen Sie das 8-Königinnen-Problem mit dem RegalRuler-Algorithmus
solution = regal_ruler(100, 1000, 0.1)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")