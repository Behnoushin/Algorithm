# Greatest Common Divisor (GCD)
# - Compute the greatest common divisor of two numbers using Euclidean algorithm.
# - Time: O(log(min(a,b))), Space: O(1)

class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
