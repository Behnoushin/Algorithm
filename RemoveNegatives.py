# Remove Negatives
# - Return a new list containing only non-negative numbers.
# - Example: [-2, 3, 0, -1, 4] → [3, 0, 4]

def removeNegatives(nums: list[int]) -> list[int]:
    return [x for x in nums if x >= 0]
