# Filter Palindrome Words
# - Given a list of words, return only palindrome words.
# - Time: O(n * m), Space: O(n)
#   where m = average length of words

class Solution:
    def filterPalindromes(self, words: list[str]) -> list[str]:
        return [w for w in words if w.lower() == w.lower()[::-1]]
