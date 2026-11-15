from typing import List


n = [3, 5, 7]

def total(numbers: List[int]) -> int:
    """Return the total of the numbers in the list."""
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum