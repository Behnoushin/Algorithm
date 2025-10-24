# Capitalize First Letter
# - Capitalize the first letter of each word in a string `s`.
# - Constraints:
#   - 1 <= len(s) <= 10^4

class Solution:
    def capitalizeFirst(self, s: str) -> str:
        return " ".join(word.capitalize() for word in s.split())
