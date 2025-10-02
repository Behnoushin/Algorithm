# Valid Palindrome
# - Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.
# - A palindrome reads the same forward and backward.
# - Convert uppercase letters to lowercase and remove all non-alphanumeric characters before checking.
# - Constraints:
#   - 1 <= s.length <= 2 * 10^5
#   - `s` consists only of printable ASCII characters.

def isPalindrome(s: str) -> bool:
    cleaned = ""
    for ch in s:
        if ch.isalnum():          
            cleaned += ch.lower()  
    
    return cleaned == cleaned[::-1]

