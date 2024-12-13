import numpy as np

def discrete_crossover(selected_population):
    """
    Perform discrete crossover on a selected population to generate offspring.
    In discrete crossover, each gene of the offspring is randomly selected from 
    one of the corresponding genes of the parents.
    Args:
        selected_population (list of lists): A list where each element is a list 
                                             representing an individual in the population. 
                                             The population size should be even.
    Returns:
        (list of lists): A list of offspring generated from the selected population. Each 
                       offspring is a combination of genes from two parents.
    """

    offspring = []
    for i in range(0, len(selected_population), 2):
        p1, p2 = selected_population[i], selected_population[i+1]
        rd_values = np.random.randint(0, 2, len(p1))
        c1, c2 = [], []
        for j in range(len(p1)):
            if rd_values[j] == 0:
                c1.append(p1[j])
                c2.append(p2[j])
            else:
                c1.append(p2[j])
                c2.append(p1[j])
        offspring.extend([c1, c2])
    return offspring
    