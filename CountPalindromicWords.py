# Count Palindromic Words
# - Given a string s containing words separated by spaces,
#   count how many words are palindromes (words that read the same forward and backward, case-insensitive).
# - Return the count as an integer.
# - Time: O(n * m), Space: O(1) where n is number of words, m is average word length

class Solution:
    def countPalindromicWords(self, s: str) -> int:
        words = s.split()
        count = 0
        for word in words:
            cleaned = word.lower()
            if cleaned == cleaned[::-1]:
                count += 1
        return count
