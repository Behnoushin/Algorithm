# Filter Words Starting With Vowel
# - Given a list of words, return only those that start with a vowel.
# - Time: O(n), Space: O(n)

class Solution:
    def filterStartingWithVowel(self, words: list[str]) -> list[str]:
        vowels = set("aeiouAEIOU")
        return [w for w in words if w and w[0] in vowels]
