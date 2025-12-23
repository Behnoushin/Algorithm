# Sum Positive Numbers
# Return the sum of all positive integers in the list.

class Solution:
    def sumPositive(self, nums: list) -> int:
        total = 0
        for num in nums:
            if isinstance(num, int) and num > 0:
                total += num
        return total
