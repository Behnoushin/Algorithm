# Average Of Positive Numbers
# - Given a list of numbers, calculate the average of positive numbers only.
# - Example: [3, -2, 5, -1, 4] → 4

from typing import List

def averageOfPositive(nums: List[int]) -> float:
    positives = [x for x in nums if x > 0]
    if not positives:
        return 0
    return sum(positives) / len(positives)
