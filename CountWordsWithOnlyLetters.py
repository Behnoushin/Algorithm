# Count Words With Only Letters
# - Given a string s containing words separated by spaces,
#   count how many words contain only alphabetic letters (a-z, A-Z).
# - Return the count as an integer.
# - Time: O(n * m), Space: O(1) where n is number of words, m is average word length

class Solution:
    def countWordsWithOnlyLetters(self, s: str) -> int:
        words = s.split()
        count = 0
        for word in words:
            if word.isalpha():
                count += 1
        return count
