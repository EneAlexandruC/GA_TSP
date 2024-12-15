import random
import numpy as np
from sklearn.manifold import MDS

def generate_mds_coordinates(distance_matrix, city_names):
    """
    Generates Multi-Dimensional Scaling (MDS) coordinates for the distance matrix.
    Parameters:
        distance_matrix (2D array): A precomputed distance matrix representing the 
                                      dissimilarities between cities.
        city_names (list of str): A list of city names corresponding to the rows/columns
                                  of the distance matrix.
    Returns:
        (dict): A dictionary where the keys are city names and the values are tuples representing 
                the coordinates in the two-dimensional space.
    """

    # The MDS instance is initialized with n_components=2, indicating that the data will 
    # be reduced to two dimensions. The dissimilarity parameter is set to "precomputed", 
    # meaning that the input distance matrix is already computed and will be used directly. 
    # The random_state=42 parameter ensures that the results are reproducible by setting a 
    # seed for the random number generator.

    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=42)

    # This method computes the coordinates of the points in the two-dimensional space based
    # on the provided distance matrix.

    coords = mds.fit_transform(distance_matrix)

    # Map coordinates to city names using dictionary comprehension.
    return {city: tuple(coord) for city, coord in zip(city_names, coords)}

def create_distance_matrix(city_names, adjacency_list):
    """
    Creates a distance matrix between all cities and their corresponding neigbors.
    Parameters:
        city_names (list of str): A list of city names.
        adjacency_list (dict): A dictionary where keys are city names and values are lists of tuples.
                               Each tuple contains a distance (float) and a neighboring city name (str).
    Returns:
        (numpy.ndarray): A 2D numpy array representing the distance matrix, where the element at [i, j]
                         is the distance between city i and city j. If there is no direct path between
                         two cities, the distance is set to infinity.
    """

    n = len(city_names)
    distance_matrix = np.full((n, n), 0)
    
    city_to_index = {city: idx for idx, city in enumerate(city_names)}

    for city, neighbors in adjacency_list.items():
        for distance, neighbor in neighbors:
            i, j = city_to_index[city], city_to_index[neighbor]
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    
    return distance_matrix

def generate_population(population_size):
    """
    Generates a population of chromosomes for a genetic algorithm.
    Args:
        population_size (int): The number of chromosomes to generate.
    Returns:
        (list): A list of chromosomes, where each chromosome is a list of cities in random order.
    """

    population = []
    for i in range(population_size):
        population.append(list(dist.keys()))
        random.shuffle(population[i])
    return population

def evaluate_chromosome(chromosome):
    """
    Evaluates the total distance of a given chromosome (route).
    Args:
        chromosome (list): A list of cities representing a route.
    Returns:
        (int): The total distance of the route.
    """

    distance = 0
    for i in range(len(chromosome) - 1):
        for pair in dist[chromosome[i]]:
            if pair[1] == chromosome[i + 1]:
                distance += pair[0]
                break
    return distance

dist = {
    'London': [(344, 'Paris'),
               (930, 'Berlin'),
               (1264, 'Madrid'),
               (1430, 'Rome'),
               (1235, 'Vienna'),
               (357, 'Amsterdam'),
               (320, 'Brussels'),
               (1035, 'Prague'),
               (1450, 'Budapest'),
               (1445, 'Warsaw'),
               (918, 'Munich'),
               (1147, 'Barcelona'),
               (950, 'Copenhagen'),
               (463, 'Dublin')],
    'Paris': [(344, 'London'),
              (878, 'Berlin'),
              (1053, 'Madrid'),
              (1105, 'Rome'),
              (1033, 'Vienna'),
              (430, 'Amsterdam'),
              (308, 'Brussels'),
              (885, 'Prague'),
              (1240, 'Budapest'),
              (1357, 'Warsaw'),
              (684, 'Munich'),
              (834, 'Barcelona'),
              (1029, 'Copenhagen'),
              (779, 'Dublin')],
    'Berlin': [(930, 'London'),
               (878, 'Paris'),
               (1862, 'Madrid'),
               (1181, 'Rome'),
               (523, 'Vienna'),
               (655, 'Amsterdam'),
               (761, 'Brussels'),
               (280, 'Prague'),
               (689, 'Budapest'),
               (518, 'Warsaw'),
               (585, 'Munich'),
               (1493, 'Barcelona'),
               (355, 'Copenhagen'),
               (1316, 'Dublin')],
    'Madrid': [(1264, 'London'),
               (1053, 'Paris'),
               (1862, 'Berlin'),
               (1363, 'Rome'),
               (1809, 'Vienna'),
               (1481, 'Amsterdam'),
               (1321, 'Brussels'),
               (1772, 'Prague'),
               (1975, 'Budapest'),
               (2275, 'Warsaw'),
               (1644, 'Munich'),
               (505, 'Barcelona'),
               (2071, 'Copenhagen'),
               (1447, 'Dublin')],
    'Rome': [(1430, 'London'),
             (1105, 'Paris'),
             (1181, 'Berlin'),
             (1363, 'Madrid'),
             (765, 'Vienna'),
             (1292, 'Amsterdam'),
             (1172, 'Brussels'),
             (923, 'Prague'),
             (811, 'Budapest'),
             (1316, 'Warsaw'),
             (697, 'Munich'),
             (862, 'Barcelona'),
             (1537, 'Copenhagen'),
             (1900, 'Dublin')],
    'Vienna': [(1235, 'London'),
               (1033, 'Paris'),
               (523, 'Berlin'),
               (1809, 'Madrid'),
               (765, 'Rome'),
               (935, 'Amsterdam'),
               (940, 'Brussels'),
               (252, 'Prague'),
               (243, 'Budapest'),
               (556, 'Warsaw'),
               (355, 'Munich'),
               (1434, 'Barcelona'),
               (870, 'Copenhagen'),
               (1649, 'Dublin')],
    'Amsterdam': [(357, 'London'),
                  (430, 'Paris'),
                  (655, 'Berlin'),
                  (1481, 'Madrid'),
                  (1292, 'Rome'),
                  (935, 'Vienna'),
                  (173, 'Brussels'),
                  (883, 'Prague'),
                  (1134, 'Budapest'),
                  (1147, 'Warsaw'),
                  (700, 'Munich'),
                  (1239, 'Barcelona'),
                  (620, 'Copenhagen'),
                  (749, 'Dublin')],
    'Brussels': [(320, 'London'),
                 (308, 'Paris'),
                 (761, 'Berlin'),
                 (1321, 'Madrid'),
                 (1172, 'Rome'),
                 (940, 'Vienna'),
                 (173, 'Amsterdam'),
                 (873, 'Prague'),
                 (1116, 'Budapest'),
                 (1206, 'Warsaw'),
                 (705, 'Munich'),
                 (1084, 'Barcelona'),
                 (755, 'Copenhagen'),
                 (779, 'Dublin')],
    'Prague': [(1035, 'London'),
               (885, 'Paris'),
               (280, 'Berlin'),
               (1772, 'Madrid'),
               (923, 'Rome'),
               (252, 'Vienna'),
               (883, 'Amsterdam'),
               (873, 'Brussels'),
               (444, 'Budapest'),
               (522, 'Warsaw'),
               (385, 'Munich'),
               (1355, 'Barcelona'),
               (634, 'Copenhagen'),
               (1450, 'Dublin')],
    'Budapest': [(1450, 'London'),
                 (1240, 'Paris'),
                 (689, 'Berlin'),
                 (1975, 'Madrid'),
                 (811, 'Rome'),
                 (243, 'Vienna'),
                 (1134, 'Amsterdam'),
                 (1116, 'Brussels'),
                 (444, 'Prague'),
                 (545, 'Warsaw'),
                 (564, 'Munich'),
                 (1491, 'Barcelona'),
                 (989, 'Copenhagen'),
                 (1787, 'Dublin')],
    'Warsaw': [(1445, 'London'),
               (1357, 'Paris'),
               (518, 'Berlin'),
               (2275, 'Madrid'),
               (1316, 'Rome'),
               (556, 'Vienna'),
               (1147, 'Amsterdam'),
               (1206, 'Brussels'),
               (522, 'Prague'),
               (545, 'Budapest'),
               (785, 'Munich'),
               (1843, 'Barcelona'),
               (672, 'Copenhagen'),
               (1828, 'Dublin')],
    'Munich': [(918, 'London'),
               (684, 'Paris'),
               (585, 'Berlin'),
               (1644, 'Madrid'),
               (697, 'Rome'),
               (355, 'Vienna'),
               (700, 'Amsterdam'),
               (705, 'Brussels'),
               (385, 'Prague'),
               (564, 'Budapest'),
               (785, 'Warsaw'),
               (1066, 'Barcelona'),
               (841, 'Copenhagen'),
               (1414, 'Dublin')],
    'Barcelona': [(1147, 'London'),
                  (834, 'Paris'),
                  (1493, 'Berlin'),
                  (505, 'Madrid'),
                  (862, 'Rome'),
                  (1434, 'Vienna'),
                  (1239, 'Amsterdam'),
                  (1084, 'Brussels'),
                  (1355, 'Prague'),
                  (1491, 'Budapest'),
                  (1843, 'Warsaw'),
                  (1066, 'Munich'),
                  (1685, 'Copenhagen'),
                  (1469, 'Dublin')],
    'Copenhagen': [(950, 'London'),
                   (1029, 'Paris'),
                   (355, 'Berlin'),
                   (2071, 'Madrid'),
                   (1537, 'Rome'),
                   (870, 'Vienna'),
                   (620, 'Amsterdam'),
                   (755, 'Brussels'),
                   (634, 'Prague'),
                   (989, 'Budapest'),
                   (672, 'Warsaw'),
                   (841, 'Munich'),
                   (1685, 'Barcelona'),
                   (1238, 'Dublin')],
    'Dublin': [(463, 'London'),
               (779, 'Paris'),
               (1316, 'Berlin'),
               (1447, 'Madrid'),
               (1900, 'Rome'),
               (1649, 'Vienna'),
               (749, 'Amsterdam'),
               (779, 'Brussels'),
               (1450, 'Prague'),
               (1787, 'Budapest'),
               (1828, 'Warsaw'),
               (1414, 'Munich'),
               (1469, 'Barcelona'),
               (1238, 'Copenhagen')]
}