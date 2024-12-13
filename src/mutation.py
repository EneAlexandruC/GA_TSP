import numpy as np

def mutation_by_change(offspring, pm):
    """
    Perform mutation by swapping two random genes in the offspring with a given probability.
    Parameters:
        offspring (list of lists): The population of offspring to be mutated. Each offspring is 
                                   represented as a list of genes.
        pm (float): The probability of mutation for each offspring.
    Returns:
        (list of lists): The mutated population of offspring.
    """
    
    rd_values = np.random.rand(len(offspring))

    for i in range(len(offspring)):
        if rd_values[i] > pm:
            continue

        rd_indices = np.random.sample(range(0, len(offspring[i])), 2)
        offspring[i][rd_indices[0]], offspring[i][rd_indices[1]] = offspring[i][rd_indices[1]], offspring[i][rd_indices[0]]
    
    return offspring

    