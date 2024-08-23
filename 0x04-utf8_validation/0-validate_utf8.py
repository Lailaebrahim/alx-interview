#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data will be represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    i = 0
    while i < len(data):
        num = data[i] & 255
        item_b = bin(num)[2:].zfill(8)
        leading_ones = len(item_b) - len(item_b.lstrip('1'))
        
        if leading_ones == 0:
            i += 1
            continue
        
        if leading_ones == 1 or leading_ones > 4 or i + leading_ones > len(data):
            return False
        
        for j in range(1, leading_ones):
            k = i + j
            item_b = bin(data[k])[2:].zfill(8)
            if not item_b.startswith('10'):
                return False
        
        i += leading_ones
    
    return True


print(validUTF8([240, 188, 128, 167]))
