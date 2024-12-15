from utils import *
from selection import *
from crossover import discrete_crossover
from mutation import mutation_by_change
from GUI import plot_route

POP_SIZE = 20
GENERATIONS = 5
population = generate_population(POP_SIZE)
distance_matrix = create_distance_matrix(list(dist.keys()), dist)
initial_city_coordinates = generate_mds_coordinates(distance_matrix, list(dist.keys()))

for _ in range(GENERATIONS):
    selected_population = fitness_proportionate_selection(population, POP_SIZE//2)
    offspring = discrete_crossover(selected_population)
    mutated_offspring = mutation_by_change(offspring, 0.5)
    population.extend(mutated_offspring)
    population = fitness_proportionate_selection(population, POP_SIZE)

    #TODO:  Need to extract the best chromosome from the population
    #       and plot it

    best_chromosome, best_distance = select_best_chromosome(population)
    route = generate_mds_coordinates(distance_matrix, best_chromosome)
    
    #TODO:  Plotting the best and worst chromosome in the population
    #       after each generation, along with their fitness values.

    plot_route(initial_city_coordinates, route , _, best_distance)
