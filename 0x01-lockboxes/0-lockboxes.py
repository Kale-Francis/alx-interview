#!/usr/bin/python3
"""
Module for Lockboxes project.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each inner list represents a box
                               and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes) # FIX 1: Removed the comma here
    opened_boxes = set()
    keys_available = []

    # Start with the first box (box 0 is unlocked)
    opened_boxes.add(0)
    # Add all keys from box 0 to the list of keys to check
    keys_available.extend(boxes[0])

    # Process the keys
    while keys_available:
        # Get the first key from the list (simulating a queue behavior)
        current_key = keys_available.pop(0)

        # Check if the key is a valid box index and if the box hasn't been opened yet
        if 0 <= current_key < num_boxes and current_key not in opened_boxes:
            # If it's a valid, unopened box, 'unlock' it
            opened_boxes.add(current_key)
            # Add all keys found inside this newly opened box to keys_available
            keys_available.extend(boxes[current_key])

    # FIX 2: Moved the final check outside the while loop.
    # After the loop finishes, all reachable boxes have been opened.
    # Now, check if the count of opened boxes equals the total number of boxes.
    return len(opened_boxes) == num_boxes
