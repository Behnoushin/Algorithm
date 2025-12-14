# Replace punctuation (. , ; :) with underscore using maketrans

class Solution:
    def symbolsToUnderline(self, s: str) -> str:
        symbols = ".,;:"
        underline = "____"
        table = str.maketrans(symbols, underline)
        return s.translate(table)
