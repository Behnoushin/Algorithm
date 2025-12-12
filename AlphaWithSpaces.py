# - Check if the string contains only alphabetic characters and spaces.
# - Time: O(n), Space: O(1)

class Solution:
    def alphaWithSpaces(self, s: str) -> bool:
        return all(c.isalpha() or c.isspace() for c in s)
