# Sum of Elements at Even Indices
# Return the sum of elements at even indices (0,2,4...) in the list.

class Solution:
    def sumEvenIndex(self, nums: list[int]) -> int:
        return sum(nums[i] for i in range(0, len(nums), 2))
