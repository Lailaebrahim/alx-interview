#!/usr/bin/python3

def canUnlockAll(boxes):
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
