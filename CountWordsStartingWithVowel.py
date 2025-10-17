# Count Words Starting With Vowel
# - Given a string s containing words separated by spaces,
#   count how many words start with a vowel (a, e, i, o, u), case-insensitive.
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countWordsStartingWithVowel(self, s: str) -> int:
        vowels = "aeiouAEIOU"
        words = s.split()
        count = 0
        for word in words:
            if word and word[0] in vowels:
                count += 1
        return count
