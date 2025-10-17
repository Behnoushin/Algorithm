# Count Words With Prime Length
# - Given a string s containing words separated by spaces,
#   count how many words have a length that is a prime number.
# - Return the count as an integer.
# - Time: O(n * sqrt(m)), Space: O(1) where n is number of words, m is average word length

class Solution:
    def countWordsWithPrimeLength(self, s: str) -> int:

        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        words = s.split()
        count = 0
        for word in words:
            if is_prime(len(word)):
                count += 1
        return count
