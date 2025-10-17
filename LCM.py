# Least Common Multiple (LCM)
# - Compute the LCM of two numbers using GCD.
# - Time: O(log(min(a,b))), Space: O(1)

class Solution:
    def lcm(self, a: int, b: int) -> int:
        from math import gcd
        return abs(a * b) // gcd(a, b)
