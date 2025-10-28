# Count Words With Length Greater Than Average
# - Given a string s containing words separated by spaces,
#   count how many words have length greater than the average length of all words.
# - Return the count as an integer.
# - Time: O(n), Space: O(1) where n is the number of words

class Solution:
    def countWordsLongerThanAverage(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0

        total_length = sum(len(word) for word in words)
        average_length = total_length / len(words)

        count = 0
        for word in words:
            if len(word) > average_length:
                count += 1
        return count
