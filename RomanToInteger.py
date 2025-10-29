# Roman To Integer
# - Convert a Roman numeral string into an integer.
# - Valid symbols: I, V, X, L, C, D, M
# - Constraints:
#   - 1 <= s.length <= 15
#   - s contains only valid Roman numerals.

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for char in reversed(s):
            curr = values[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
