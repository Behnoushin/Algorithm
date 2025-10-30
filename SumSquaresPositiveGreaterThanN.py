# Sum Squares Positive Greater Than N
# - Given a list of integers and a number N
# - Filter positive numbers greater than N
# - Square each filtered number
# - Return the sum of these squares
# - Example: nums = [1, 3, -2, 5, 7], N = 3 → 5² + 7² = 25 + 49 = 74

class Solution:
    def sumSquaresPositiveGreaterThanN(self, nums: list[int], N: int) -> int:
        result = 0
        for x in nums:
            if x > N and x > 0:      
                result += x * x  
        return result
