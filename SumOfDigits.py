# Sum of Digits
# - Given an integer n, return the sum of its digits.
# - Example: 123 -> 1 + 2 + 3 = 6
# - Can be solved recursively or using loops.

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
