from utils import evaluate_chromosome
import numpy as np

def select_best_chromosome(population):
    """
    Select the best chromosome from the population based on their fitness values.
    Args:
        population (list): A list of chromosomes representing the population.
    Returns:
        (list), int: The best chromosome from the population.
    """

    fitness = [evaluate_chromosome(chromosome) for chromosome in population]
    best_index = np.argmin(fitness)
    return population[best_index], fitness[best_index]

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

    selected_indices = np.random.choice(len(population), size=size, p=p, replace=False)

    return [population[i] for i in selected_indices]