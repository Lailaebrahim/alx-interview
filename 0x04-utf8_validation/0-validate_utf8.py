#!/usr/bin/python3
"""_summary_  a method that determines if a given data set represents a valid UTF-8 encoding.
"""
def validUTF8(data):
    """_summary_

    Args:
        data (list of intgers): The data will be represented by a list of integers
    """
    for i in range(len(data)):
        num = data[i] & 255
        item_b = bin(num)[2:].zfill(8)
        leading_ones = len(item_b) - len(item_b.lstrip('1'))
        if leading_ones == 0:
            continue
        if leading_ones == 1 or leading_ones > 4 or i + leading_ones > len(data):
            return False
        
        for j in range(leading_ones - 1):
            k = i + j + 1
            item_b = bin(data[k])[2:].zfill(8)
            if not item_b.startswith('10'):
                return False
    return True
