# Average Of Even Numbers
# - Given a list of numbers, calculate the average of even numbers only.
# - Example: [1, 2, 3, 4, 5, 6] → 4

from typing import List

def averageOfEvens(nums: List[int]) -> float:
    evens = [x for x in nums if x % 2 == 0]
    if not evens:
        return 0
    return sum(evens) / len(evens)
