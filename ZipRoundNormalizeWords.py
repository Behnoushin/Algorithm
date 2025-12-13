# - Normalize words (strip, remove punctuation, fix spaces).
# - Capitalize each word.
# - Zip with number list.
# - Round the sum of (len(word) + number).
# - Time: O(n), Space: O(n)

class Solution:
    def zipRoundNormalizeWords(self, words: list[str], nums: list[int]):
        clean_words = []

        for w in words:
            w = w.strip()
            w = "".join(ch for ch in w if ch.isalnum() or ch.isspace())
            w = w.replace("  ", " ").capitalize()
            clean_words.append(w)

        result = []
        for w, n in zip(clean_words, nums):
            total = len(w) + n
            result.append(round(total, 1))

        return result
