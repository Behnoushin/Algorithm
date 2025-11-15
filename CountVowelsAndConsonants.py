# CountVowelsAndConsonants
# - Given a string s, count vowels and consonants.
# - Return a tuple (vowels_count, consonants_count).
# - Time: O(n), Space: O(1)

class Solution:
    def countVowelsAndConsonants(self, s: str) -> tuple[int, int]:
        vowels = "aeiouAEIOU"
        vCount, cCount = 0, 0
        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    vCount += 1
                else:
                    cCount += 1
        return (vCount, cCount)
