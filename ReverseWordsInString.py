# Reverse Words in a String III
# - Given a string `s`, reverse the order of characters in each word while preserving whitespace and initial word order.
# - Constraints:
#   - 1 <= s.length <= 5 * 10^4
#   - s contains printable ASCII characters
#   - s does not contain leading or trailing spaces
#   - All words are separated by a single space

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)
