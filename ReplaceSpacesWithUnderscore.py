# Replace Spaces With Underscore
# - Replace all spaces in string `s` with underscores.
# - Constraints:
#   - 1 <= len(s) <= 10^4

class Solution:
    def replaceSpaces(self, s: str) -> str:
        return s.replace(" ", "_")
