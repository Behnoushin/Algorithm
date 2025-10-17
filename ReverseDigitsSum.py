# Reverse Digits and Sum
# - Reverse the digits of a number and also calculate sum of digits
# - Time: O(log10(n)), Space: O(1)

class Solution:
    def reverseDigitsAndSum(self, n: int) -> tuple[int,int]:
        original = n
        rev = 0
        total = 0
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            total += digit
            n //= 10
        return rev, total
