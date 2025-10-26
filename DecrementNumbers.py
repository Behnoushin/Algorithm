# Decrement Numbers
# - Return a list with each number decreased by 1.
# - Example: [1,2,3] → [0,1,2]

def decrementNumbers(nums: list[int]) -> list[int]:
    return [x - 1 for x in nums]
