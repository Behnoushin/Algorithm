# Sort Strings Alphabetically
# - Given a list of strings `words`, sort them in alphabetical order.
# - Constraints:
#   - 1 <= len(words) <= 10^4

from typing import List

class Solution:
    def sortAlphabetically(self, words: List[str]) -> List[str]:
        return sorted(words)
