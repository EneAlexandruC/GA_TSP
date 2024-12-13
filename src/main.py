from utils import dist, generate_population
from selection import fitness_proportionate_selection
from crossover import discrete_crossover
from mutation import mutation_by_change

POP_SIZE = 20
GENERATIONS = 100

while GENERATIONS:
    population = generate_population(POP_SIZE)
    selected_population = fitness_proportionate_selection(population, POP_SIZE//2)
    offspring = discrete_crossover(selected_population)
    mutated_offspring = mutation_by_change(offspring, 0.5)
    population.extend(mutated_offspring)
    population = fitness_proportionate_selection(population, POP_SIZE)

    #TODO:  Plotting the best and worst chromosome in the population
    #       after each generation, along with their fitness values.

    GENERATIONS -= 1
