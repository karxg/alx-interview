#!/usr/bin/python3
"""
Pascal's Triangle Script that draw a pascal triangle with a number of rows passed to the function
"""

def pascal_triangle(rows):
    """
    Generates Pascal's Triangle up to a given number of rows.

    Args:
        rows (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists containing the values of Pascal's Triangle.
              Returns an empty list if rows <= 0.
    """
    triangle = []
    if rows <= 0:
        return triangle

    triangle = [[1]]
    for row_index in range(1, rows):
        row = [1]
        previous_row = triangle[row_index - 1]
        for column_index in range(len(previous_row) - 1):
            row.append(previous_row[column_index] + previous_row[column_index + 1])
        row.append(1)
        triangle.append(row)

    return triangle
