# Sum of Numbers That Are Multiples of 3 or 5
# - Given a list of integers nums,
#   return the sum of numbers that are multiples of 3 or 5.
# - Time: O(n), Space: O(1)

class Solution:
    def sumMultiplesOf3Or5(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            if num % 3 == 0 or num % 5 == 0:
                total += num
        return total
