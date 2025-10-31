# Remove Vowels From String
# - Given a string `s`, remove all vowels (a, e, i, o, u, both cases).
# - Constraints:
#   - 1 <= len(s) <= 10^4

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        return "".join(c for c in s if c not in vowels)
