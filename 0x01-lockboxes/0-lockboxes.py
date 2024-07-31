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
    keys = []
    for box_index in range(1, len(boxes)):
        collected_keys = [keys.extend(box) for box in boxes[:box_index] + boxes[box_index + 1:]]
        if box_index in keys:
            keys = []
        else:
            return False
    return True
