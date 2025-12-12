# - Check if all words in the list are alphanumeric.
# - Time: O(n), Space: O(n)

class Solution:
    def allWordsAlnum(self, words: list[str]) -> bool:
        return all(w.isalnum() for w in words)
