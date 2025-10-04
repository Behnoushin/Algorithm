# Count Vowels
# - Given a string s, count the number of vowels (a, e, i, o, u, case-insensitive).
# - Return the count as integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countVowels(self, s: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for ch in s:
            if ch in vowels:
                count += 1
        return count
