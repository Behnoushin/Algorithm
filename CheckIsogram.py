# Check Isogram
# - Determine if a word `s` has no repeating letters.
# - Constraints:
#   - 1 <= len(s) <= 1000

class Solution:
    def isIsogram(self, s: str) -> bool:
        s = s.lower()
        seen = set()
        for c in s:
            if c.isalpha():
                if c in seen:
                    return False
                seen.add(c)
        return True
