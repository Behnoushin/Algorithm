# Sum of Squares of First N Numbers
# - Calculate sum of squares from 1 to N
# - Time: O(1) using formula, Space: O(1)

class Solution:
    def sumOfSquares(self, n: int) -> int:
        return n * (n + 1) * (2 * n + 1) // 6
