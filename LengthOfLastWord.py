# Length of Last Word
# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
# - A word is a maximal substring of non-space characters
# - Spaces at the end of the string should be ignored

def lengthOfLastWord(s: str) -> int:
    words = s.split()
    return len(words[-1])