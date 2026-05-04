"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List

def calculate_power_with_difference(ints: List[int]) -> List[int]:
    if not ints:
        return []
    
    result = []
    
    for i, num in enumerate(ints):
        square = num ** 2
        
        if i == 0:
            result.append(square)
        else:
            prev_square = ints[i - 1] ** 2
            prev_original = ints[i - 1]
            adjustment = prev_square - prev_original
            result.append(square - adjustment)
    
    return result


print(calculate_power_with_difference([1, 2, 3]))