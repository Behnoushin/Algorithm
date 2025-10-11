# Sort Words by Last Letter
# - Given a list of words, return them sorted by their last character.
# - Time: O(n log n), Space: O(n)

class Solution:
    def sortByLastLetter(self, words: list[str]) -> list[str]:
        return sorted(words, key=lambda w: w[-1])
