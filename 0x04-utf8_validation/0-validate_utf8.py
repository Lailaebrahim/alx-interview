#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int):data will be represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    i = 0
    while i < len(data):
        num = data[i] & 255
        item_b = bin(num)[2:].zfill(8)
        lead_ones = len(item_b) - len(item_b.lstrip('1'))

        if lead_ones == 0:
            i += 1
            continue

        if lead_ones == 1 or lead_ones > 4 or i + lead_ones > len(data):
            return False

        for j in range(1, lead_ones):
            k = i + j
            item_b = bin(data[k])[2:].zfill(8)
            if not item_b.startswith('10'):
                return False

        i += lead_ones

    return True
