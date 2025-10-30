# SquareEvenNumbers
# - Given a list of integers, return a new list containing only even numbers squared.

def squareEvenNumbers(nums: list[int]) -> list[int]:
    return [x ** 2 for x in nums if x % 2 == 0]
