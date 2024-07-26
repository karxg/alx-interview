#!/usr/bin/python3
"""
Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:  # If n is less than or equal to 0, return an empty list.
        return []
    Triangle = []
    for i in range(n):  # Iterate over the range from 0 to n-1.
        if i == 0:
            Triangle.append([1])
        elif i == 1:
            Triangle.append([1, 1])
        else:
            row = [1]  # Start each new row with 1.
            for x in range(1, len(Triangle[i - 1])):

                row.append(Triangle[i - 1][x] + Triangle[i - 1][x - 1])
            row.append(1)  # End every row with 1.
            Triangle.append(row.copy())
            row.clear()  # Clear row list

    return Triangle  # Return the Pascal's Triangle.
