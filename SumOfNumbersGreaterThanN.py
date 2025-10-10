# Sum of Numbers Greater Than N
# - Given a list of integers nums and an integer N,
#   return the sum of numbers greater than N.
# - Time: O(n), Space: O(1)

class Solution:
    def sumGreaterThanN(self, nums: list[int], N: int) -> int:
        total = 0
        for num in nums:
            if num > N:
                total += num
        return total
