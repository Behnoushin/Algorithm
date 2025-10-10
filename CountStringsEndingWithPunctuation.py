# Count Strings Ending With Punctuation
# - Given a list of strings, count how many strings end with a punctuation mark (.,!?, etc.).
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

import string

class Solution:
    def countStringsEndingWithPunctuation(self, strs: list[str]) -> int:
        count = 0
        for s in strs:
            if s and s[-1] in string.punctuation:
                count += 1
        return count
