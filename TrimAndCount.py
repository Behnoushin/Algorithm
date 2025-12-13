# - Remove spaces from both sides and return length

class Solution:
    def trimmedLength(self, s: str) -> int:
        return len(s.strip())
