# The Wagner–Fischer algorithm is a dynamic programming algorithm
# that computes the edit distance between two strings of characters.

import numpy as np


def load_values():
    return ['кто']


def count_distances(value, strings):
    result = []
    for string in strings:
        result.append(count_distance(value, string))
    return result


def count_distance(a, b):
    m = len(a)
    n = len(b)
    d = np.empty((m + 1, n + 1))
    # Расстояние от источника до пустой строки цели вычисляется удалением всех символов
    for i in range(1, m):
        d[i, 0] = i
    # Расстояние от цели до пустого источника вычисляется добавлением всех символов
    for j in range(1, n):
        d[0, j] = j
    for j in range(1, n):
        for i in range(1, m):
            if a[i] == b[j]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            d[i, j] = min(d[i - 1, j] + 1,  # deletion
                          d[i, j - 1] + 1,  # insertion
                          d[i - 1, j - 1] + substitution_cost)  # substitution
    return d[m - 1, n - 1]


if __name__ == '__main__':
    inp = 'кот'
    print(count_distances(inp, load_values()))
