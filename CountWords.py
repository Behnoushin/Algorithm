# Count Words
# - Given a string s, count the number of words separated by spaces.
# - A word is defined as a sequence of non-space characters.
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countWords(self, s: str) -> int:
        words = s.split()
        return len(words)
