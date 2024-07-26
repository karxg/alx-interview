#!/usr/bin/python3
"""
Create Pascal's Triangle up to a specified number of rows.

    Args:
        rows (int): The number of rows to generate for Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
"""


def pascal_triangle(rows):
    """
    Create Pascal's Triangle up to a specified number of rows.

    Args:
        rows (int): The number of rows to generate for Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if rows <= 0:  # If rows is less than or equal to 0, return an empty list.
        return []
    triangle = []
    for row_num in range(rows):  # Iterate over the range from 0 to rows-1.
        if row_num == 0:
            triangle.append([1])  # The first row is always [1].
        elif row_num == 1:
            triangle.append([1, 1])  # The second row is always [1, 1].
        else:
            current_row = [1]  # Start each new row with 1.
            for j in range(1, len(triangle[row_num - 1])):
                # Append the sum of the two elements above the current
                current_row.append(triangle[row_num - 1][j] + triangle[row_num - 1][j - 1])
            current_row.append(1)  # End each row with 1.
            triangle.append(current_row.copy())
            current_row.clear()  # Clear the current_row list

    return triangle  # Return the complete Pascal's Triangle.
