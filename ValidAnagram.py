# Valid Anagram
# Given two strings s and t, return True if t is an anagram of s, otherwise False.
# - An anagram means t has exactly the same letters as s, just rearranged
# - Both s and t consist of lowercase English letters

from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)