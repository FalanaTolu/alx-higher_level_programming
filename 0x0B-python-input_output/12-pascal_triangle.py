#!/usr/bin/python3
"""Module for 12-pascal_triangle."""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    tri = [[0 for x in range(i + 1)] for i in range(n)]
    tri[0] = [1]

    for i in range(1, n):
        tri[i][0] = 1
        for j in range(1, i + 1):
            if j < len(tri[i - 1]):
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
            else:
                tri[i][j] = tri[i - 1][0]
    return tri
