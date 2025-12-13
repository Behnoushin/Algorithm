# - If the string contains spaces, return it in title case
# - Otherwise return it unchanged

class Solution:
    def titleIfSentence(self, s: str) -> str:
        if " " in s:
            return s.title()
        return s
