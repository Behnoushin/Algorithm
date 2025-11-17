# Multiply Each Number by 2
# - Given a list of numbers, return a new list where each number is multiplied by 2.
# - Example: [1, 2, 3, 4] → [2, 4, 6, 8]

from typing import List

def multiplyByTwo(nums: List[int]) -> List[int]:
    return [x*2 for x in nums]
