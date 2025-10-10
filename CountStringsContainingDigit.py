# Count Strings Containing Digit
# - Given a list of strings, count how many strings contain at least one digit.
# - Return the count as an integer.
# - Time: O(n * m), Space: O(1) where n is number of strings, m is average string length.

class Solution:
    def countStringsWithDigit(self, strs: list[str]) -> int:
        count = 0
        for s in strs:
            if any(ch.isdigit() for ch in s):
                count += 1
        return count
