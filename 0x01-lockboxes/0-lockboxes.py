#!/usr/bin/python3
"""
Lockboxes Module
This module provides a function to determine if all lockboxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determine if all lockboxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each inner list contains the keys
                                     to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    keys_collected = set()  # To store collected keys
    keys_collected.add(0)  # The first box is always unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in keys_collected:
                keys_collected.add(key)
                if key < len(boxes):
                    stack.append(key)

    return len(keys_collected) == len(boxes)
