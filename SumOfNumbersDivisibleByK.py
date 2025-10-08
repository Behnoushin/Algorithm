# Sum of Numbers Divisible by K
# - Given a list of integers nums and an integer K,
#   return the sum of numbers divisible by K.
# - Time: O(n), Space: O(1)

class Solution:
    def sumDivisibleByK(self, nums: list[int], K: int) -> int:
        total = 0
        for num in nums:
            if num % K == 0:
                total += num
        return total
