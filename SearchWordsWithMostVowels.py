# Search Words With Most Vowels
# - Return the word with the highest number of vowels.
# - If multiple words have same max vowels, return the first one.
# - Time: O(n * m), Space: O(1), m = average word length

class Solution:
    def searchWordWithMostVowels(self, words: list[str]) -> str:
        vowels = set("aeiouAEIOU")
        max_count = -1
        result = ""
        for w in words:
            count = sum(1 for ch in w if ch in vowels)
            if count > max_count:
                max_count = count
                result = w
        return result
