# Remove Punctuation
# - Remove all punctuation characters from a string `s`.
# - Constraints:
#   - 1 <= len(s) <= 10^4

import string

class Solution:
    def removePunctuation(self, s: str) -> str:
        return "".join(c for c in s if c not in string.punctuation)
