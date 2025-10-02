# Palindrome Number
# - Given an integer `x`, return `True` if `x` is a palindrome, otherwise `False`.
# - Negative numbers are not palindromes.
# - Follow up: solve it without converting the integer to a string.

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    return original == reversed_num