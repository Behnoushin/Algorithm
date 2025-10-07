# Count Unique Characters
# - Given a string s, count how many unique characters appear in it.
# - Return the count as an integer.
# - Time: O(n), Space: O(k) where k is the number of unique characters.

class Solution:
    def countUniqueChars(self, s: str) -> int:
        unique_chars = set()
        for ch in s:
            unique_chars.add(ch)
        return len(unique_chars)
