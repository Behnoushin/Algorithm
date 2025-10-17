# Find Longest String in List
# - Given a list of strings strs, return the longest string.
# - Time: O(n), Space: O(1)

class Solution:
    def findLongestString(self, strs: list[str]) -> str:
        if not strs:
            return ""
        longest = strs[0]
        for s in strs[1:]:
            if len(s) > len(longest):
                longest = s
        return longest
