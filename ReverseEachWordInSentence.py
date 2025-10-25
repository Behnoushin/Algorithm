# Reverse Each Word In Sentence
# - Reverse each word in a string `s` while keeping word order.
# - Constraints:
#   - 1 <= len(s) <= 10^4

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())
