# Sort Strings By Length
# - Given a list of strings `words`, sort them by their length in ascending order.
# - Constraints:
#   - 1 <= len(words) <= 10^4

from typing import List

class Solution:
    def sortByLength(self, words: List[str]) -> List[str]:
        return sorted(words, key=len)
