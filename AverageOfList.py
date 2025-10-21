# Average Of List
# - Given a list of numbers, calculate and return their average value.
# - Example: [2, 4, 6, 8] → 5

from typing import List

def averageOfList(nums: List[float]) -> float:
    if not nums:
        return 0
    return sum(nums) / len(nums)
