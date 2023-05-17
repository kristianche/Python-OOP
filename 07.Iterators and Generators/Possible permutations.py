from itertools import permutations


def possible_permutations(sequence):
    for el in list(permutations(sequence)):
        yield list(el)