# Fizz Buzz
# Given an integer n, return a list of strings from 1 to n following these rules:
# - If a number is divisible by 3 and 5, add "FizzBuzz"
# - If a number is divisible by 3 only, add "Fizz"
# - If a number is divisible by 5 only, add "Buzz"
# - Otherwise, add the number itself as a string

def fizzBuzz(self, n: int):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result