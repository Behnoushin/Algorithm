# Count Consonants
# - Given a string `s`, count all consonant letters.
# - Constraints:
#   - 1 <= len(s) <= 10^4

class Solution:
    def countConsonants(self, s: str) -> int:
        return sum(1 for c in s if c.isalpha() and c.lower() not in "aeiou")
