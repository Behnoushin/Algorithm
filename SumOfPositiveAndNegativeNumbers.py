# Sum of Positive and Negative Numbers
# - Given a list of integers, calculate the sum of positive numbers
#   and the sum of negative numbers separately.

from typing import List, Tuple

def sum_positive_negative(nums: List[int]) -> Tuple[int, int]:
    positive_sum = 0
    negative_sum = 0

    for num in nums:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    return positive_sum, negative_sum


