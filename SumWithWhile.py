# Sum Using While
# Return the sum of all numbers in the list using a while loop.

class Solution:
    def sumWithWhile(self, nums: list[int]) -> int:
        total = 0
        i = 0
        while i < len(nums):
            total += nums[i]
            i += 1
        return total
