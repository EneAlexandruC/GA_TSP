from utils import *
from selection import *
from crossover import discrete_crossover
from mutation import mutation_by_change
from GUI import *

POP_SIZE = 200
GENERATIONS = 100
MUTATION_PROBABILITY = 0.2

@profiler
def main():
    population = generate_population(POP_SIZE)
    distance_matrix = create_distance_matrix(list(dist.keys()), dist)
    initial_city_coordinates = generate_mds_coordinates(distance_matrix, list(dist.keys()))
    best_routes, best_distances, worst_routes, worst_distances = [], [], [], []
    med_routes, med_distances = [], []
    values = []

    for _ in range(GENERATIONS):
        selected_population = fitness_proportionate_selection(population, POP_SIZE)
        offspring = discrete_crossover(selected_population)
        mutated_offspring = mutation_by_change(offspring, MUTATION_PROBABILITY)
        population.extend(mutated_offspring)
        population = best_performer_selection(population)

        #TODO:  Need to extract the best chromosome from the population
        #       and plot it

        med_chromosome, med_distance, fitness = select_med_chromosome(population)
        values.append(fitness)

        best_chromosome, best_distance, worst_chromosome, worst_distance = select_best_chromosome(population)


        worst_routes.append(generate_mds_coordinates(distance_matrix, worst_chromosome))
        worst_distances.append(worst_distance)

        med_routes.append(generate_mds_coordinates(distance_matrix, med_chromosome))
        med_distances.append(med_distance)

        best_routes.append(generate_mds_coordinates(distance_matrix, best_chromosome))
        best_distances.append(best_distance)

    #TODO:  Plotting the best and worst chromosome in the population
    #       after each generation, along with their fitness values.
    
    plot_dispersion(values)
    plot_median(values)

    plot_worst_routes_animation(initial_city_coordinates,
                                worst_routes,
                                [_ for _ in range(GENERATIONS)],
                                worst_distances
                                )
    
    plot_median_routes_animation(initial_city_coordinates, 
                                 med_routes, 
                                 [_ for _ in range(GENERATIONS)],
                                 med_distances
                                 )

    plot_best_routes_animation(initial_city_coordinates,
                               best_routes,
                               [_ for _ in range(GENERATIONS)],
                               best_distances
                               )

if __name__ == "__main__":
    main()

#TODO:  dispersia, selectie turneu?, medie populatie,
#       incrucisarea, distanta medie la fiecare gen grafic, grafic dispersie