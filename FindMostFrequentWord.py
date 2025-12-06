# Find Most Frequent Word
# - Find the word that appears most frequently in a string `s`.
# - If multiple, return the first one.
# - Constraints:
#   - 1 <= len(s) <= 10^4

from collections import Counter

class Solution:
    def mostFrequentWord(self, s: str) -> str:
        words = s.split()
        counts = Counter(words)
        max_count = max(counts.values())
        for word in words:
            if counts[word] == max_count:
                return word
