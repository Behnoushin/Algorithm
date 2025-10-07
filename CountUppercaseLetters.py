# Count Uppercase Letters
# - Given a string s, count the number of uppercase letters (A–Z).
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countUppercase(self, s: str) -> int:
        count = 0
        for ch in s:
            if ch.isupper():
                count += 1
        return count
