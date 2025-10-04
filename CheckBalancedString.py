# Check Balanced String
# - Given a string num consisting only of digits.
# - A string is balanced if the sum of digits at even indices equals the sum at odd indices.
# - Return true if balanced, otherwise false.
# - Time: O(n), Space: O(1)

class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0

        for i, ch in enumerate(num):
            digit = int(ch)
            if i % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit

        return even_sum == odd_sum
