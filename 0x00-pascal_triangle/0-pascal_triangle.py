#!/usr/bin/python3
"""
Pascal's Triangle Script that draws a Pascal triangle with a number of rows passed to the function.
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
    triangle = []  # Initialize an empty list to hold the triangle.

    if rows <= 0:  # If the number of rows is less than or equal to 0, return an empty list.
        return triangle

    triangle = [[1]]  # Initialize the triangle with the first row containing a single 1.

    for row_index in range(1, rows):
        row = [1]  # Start each new row with 1.
        previous_row = triangle[row_index - 1]  # Get the previous row to calculate the new values.

        for column_index in range(len(previous_row) - 1):
            # Append the sum of the two elements above the current position in the new row.
            row.append(previous_row[column_index] + previous_row[column_index + 1])

        row.append(1)  # End each row with 1.
        triangle.append(row)  # Add the completed row to the triangle.

    return triangle  # Return the complete Pascal's Triangle.
