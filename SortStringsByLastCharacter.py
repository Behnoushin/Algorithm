# Sort Strings By Last Character
# - Given a list of strings `words`, sort them based on the last character of each string.
# - Constraints:
#   - 1 <= len(words) <= 10^4

from typing import List

class Solution:
    def sortByLastChar(self, words: List[str]) -> List[str]:
        return sorted(words, key=lambda x: x[-1])
