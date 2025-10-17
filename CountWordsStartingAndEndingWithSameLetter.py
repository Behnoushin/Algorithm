# Count Words Starting And Ending With Same Letter
# - Given a string s containing words separated by spaces,
#   count how many words start and end with the same letter (case-insensitive).
# - Return the count as an integer.
# - Time: O(n), Space: O(1) where n is number of words

class Solution:
    def countWordsSameStartEnd(self, s: str) -> int:
        words = s.split()
        count = 0
        for word in words:
            if word and word[0].lower() == word[-1].lower():
                count += 1
        return count
