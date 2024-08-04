#!/usr/bin/python3
"""
Summary module to define method can_unlock_all.
"""

def can_unlock_all(boxes):
  """
  Determines if all the boxes in the list can be unlocked.
  Args:
    boxes (list): A list of lists representing the boxes and their corresponding keys.
  Returns:
    bool: True if all the boxes can be unlocked, False otherwise.
  """
  unlocked = [False] * len(boxes)
  unlocked[0] = True
  keys = [0]  # Start with the keys from the first box

  while keys:
    current_key = keys.pop()
    for new_key in boxes[current_key]:
      if new_key < len(boxes) and not unlocked[new_key]:
        unlocked[new_key] = True
        keys.append(new_key)

  return all(unlocked)
