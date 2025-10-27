# Sum of Even Numbers in Array
# - Given an array of integers, calculate and return the sum of all even numbers.
# - Time complexity: O(n)
# - Example: [3, 8, 5, 12, 7, 4, 9, 6] → Output: 30

from typing import List

def sum_even_numbers(arr: List[int]) -> int:
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total


