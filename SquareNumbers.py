# Square Numbers
# - Return a list with each number squared.
# - Example: [1,2,3] → [1,4,9]

def squareNumbers(nums: list[int]) -> list[int]:
    return [x**2 for x in nums]
