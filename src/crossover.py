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

    #TODO: Make the routes not have duplicate cities


    offspring = []
    for i in range(0, len(selected_population), 2):
        p1, p2 = selected_population[i], selected_population[i+1]
        rd_values = np.random.randint(0, 2, len(p1))
        c1, c2 = [], []
        # Ensure no duplicates in c1 and c2 and maintain the size of the parents
        c1_set, c2_set = set(c1), set(c2)
        for j in range(len(p1)):
            if rd_values[j] == 0:
                if p2[j] not in c1_set and len(c1) < len(p1):
                    c1.append(p2[j])
                    c1_set.add(p2[j])
                if p1[j] not in c2_set and len(c2) < len(p1):
                    c2.append(p1[j])
                    c2_set.add(p1[j])
            else:
                if p1[j] not in c1_set and len(c1) < len(p1):
                    c1.append(p1[j])
                    c1_set.add(p1[j])
                if p2[j] not in c2_set and len(c2) < len(p1):
                    c2.append(p2[j])
                    c2_set.add(p2[j])
        # Fill in any missing genes to maintain the size of the parents
        for gene in p1:
            if len(c1) < len(p1) and gene not in c1_set:
                c1.append(gene)
                c1_set.add(gene)
            if len(c2) < len(p1) and gene not in c2_set:
                c2.append(gene)
                c2_set.add(gene)

        for gene in p2:
            if len(c1) < len(p2) and gene not in c1_set:
                c1.append(gene)
                c1_set.add(gene)
            if len(c2) < len(p2) and gene not in c2_set:
                c2.append(gene)
                c2_set.add(gene)
        offspring.extend([c1, c2])
    return offspring
    