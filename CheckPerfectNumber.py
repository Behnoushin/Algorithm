# Check Perfect Number
# - A perfect number is a number equal to the sum of its proper divisors.
# - Time: O(sqrt(n)), Space: O(1)

class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n < 2:
            return False
        total = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total == n
