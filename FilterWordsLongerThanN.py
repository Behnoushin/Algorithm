# Filter Words Longer Than N
# - Given a list of words and a number n, return words longer than n.
# - Time: O(n), Space: O(n)

class Solution:
    def filterLongWords(self, words: list[str], n: int) -> list[str]:
        return [w for w in words if len(w) > n]
