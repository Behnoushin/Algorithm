# Sum of Unique Numbers
# - Given a list of integers nums,
#   return the sum of unique numbers (ignore duplicates).
# - Time: O(n), Space: O(n)

class Solution:
    def sumUnique(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        total = 0
        for num in unique_nums:
            total += num
        return total
