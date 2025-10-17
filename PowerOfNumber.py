# Power of a Number
# - Compute a to the power of b without using ** or math.pow
# - Time: O(log b), Space: O(1) using iterative fast exponentiation

class Solution:
    def power(self, a: int, b: int) -> int:
        result = 1
        base = a
        exp = b
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        return result
