# Return substring between two characters (inclusive)

class Solution:
    def substringBetween(self, s: str, start: str, end: str) -> str:
        i = s.find(start)
        j = s.find(end)
        if i == -1 or j == -1 or i > j:
            return ""
        return s[i:j+1]
