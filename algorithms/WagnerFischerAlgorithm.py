# The Wagner–Fischer algorithm is a dynamic programming algorithm
# that computes the edit distance between two strings of characters.

import numpy as np


def load_values():
    return ['some', 'other', 'sme']


def count_distances(value, strings):
    result = []
    for string in strings:
        result.append(count_distance(value, string))
    return result


def count_distance(a, b):
    # matrix = np.empty((len(a), len(b)))
    return 0


if __name__ == '__main__':
    inp = 'some'
    print(count_distances(inp, load_values()))
