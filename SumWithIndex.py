# - Given a list of numbers, return the sum of numbers at even indices.
# - Time: O(n), Space: O(1)

class Solution:
    def sumEvenIndex(self, nums: list[int]) -> int:
        return sum(val for i, val in enumerate(nums) if i % 2 == 0)