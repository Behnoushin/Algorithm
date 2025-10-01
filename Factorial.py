# Factorial
# - Given an integer n, calculate n! = n * (n-1) * ... * 1
# - 0! = 1 by definition
# - Can be solved recursively or iteratively.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)