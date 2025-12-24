# Sum of Squares
# Return the sum of squares of all numbers in the list.

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        return sum(x**2 for x in nums)
