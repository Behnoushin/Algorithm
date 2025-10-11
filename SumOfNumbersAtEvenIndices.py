# Sum of Numbers at Even Indices
# - Given a list of integers nums,
#   return the sum of numbers at even indices (0,2,4,...).
# - Time: O(n), Space: O(1)

class Solution:
    def sumEvenIndices(self, nums: list[int]) -> int:
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
