# - Title only words that do not contain numbers

class Solution:
    def titleCleanWords(self, s: str) -> str:
        return " ".join(
            word.title() if word.isalpha() else word
            for word in s.split()
        )
