import numpy as np
from utils import evaluate_chromosome

def best_performer_selection(population):
    """
    Selects the best performing half of the population based on their fitness scores.
    Args:
        population (list): A list of chromosomes representing the population.
    Returns:
        list: A list containing the top 50% of the population based on fitness.
    """
    
    fitness = [evaluate_chromosome(chromosome) for chromosome in population]
    sorted_population = [x for _, x in sorted(zip(fitness, population))]
    return sorted_population[:len(population) // 2]

def tournament_selection(population, size, tournament_size):
    """
    Perform tournament selection on a given population.
    Args:
        population (list): A list of chromosomes representing the population.
        size (int): The number of chromosomes to select.
        tournament_size (int): The number of chromosomes to compete in each tournament.
    Returns:
        (list): A list of the selected chromosomes.
    """

    selected = []
    for _ in range(size):
        tournament = np.random.choice(population, tournament_size, replace=True)
        tournament_fitness = [evaluate_chromosome(chromosome) for chromosome in tournament]
        winner_index = np.argmin(tournament_fitness)
        selected.append(tournament[winner_index])
    return selected

def select_med_chromosome(population):
    """
    Selects the median chromosome from a given population based on their fitness.
    Args:
        population (list): A list of chromosomes, where each chromosome is a list or any other iterable.
    Returns:
        tuple: A tuple containing:
            - The median chromosome from the sorted population.
            - The fitness value of the median chromosome.
            - The list of fitness values for the entire population.
    """

    fitness = [evaluate_chromosome(chromosome) for chromosome in population]
    sorted_population = [x for _, x in sorted(zip(fitness, population))]
    sorted_fitness = sorted(fitness)

    return sorted_population[len(sorted_population) // 2], sorted_fitness[len(sorted_population) // 2], fitness

def select_best_chromosome(population):
    """
    Selects the best and worst chromosomes from a given population based on their fitness.
    Args:
        population (list): A list of chromosomes, where each chromosome is represented by a list or array.
    Returns:
        tuple: A tuple containing:
            - The best chromosome (based on minimum fitness).
            - The fitness value of the best chromosome.
            - The worst chromosome (based on maximum fitness).
            - The fitness value of the worst chromosome.
    """

    fitness = [evaluate_chromosome(chromosome) for chromosome in population]
    best_index = np.argmin(fitness)
    worst_index = np.argmax(fitness)

    return population[best_index], fitness[best_index], population[worst_index], fitness[worst_index]

def fitness_proportionate_selection(population, size):
    """
    Perform fitness proportionate selection on a given population.
    This function calculates the fitness of each chromosome in the population
    using the `evaluate_chromosome` function from the `utils` module. It then
    computes the selection probability for each chromosome based on their
    fitness values. The selection probability is inversely proportional to the
    fitness value, meaning that chromosomes with lower fitness values have
    higher selection probabilities. I used this approach because the project I've
    chosen is a minimization problem.
    Args:
        population (list): A list of chromosomes representing the population.
    Returns:
        (list): A list of the selected chromosomes.
    """
    fitness = [evaluate_chromosome(chromosome) for chromosome in population]
    p = [(1/f) for f in fitness]
    total_p = sum(p)
    p = [prob/total_p for prob in p]

    selected_indices = np.random.choice(len(population), size=size, p=p, replace=True)

    return [population[i] for i in selected_indices]