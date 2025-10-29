# Find Min-Max Difference
# - Return difference between largest and smallest number in a list.
# - Example: [3,7,2,5] → 5

def findMinMaxDifference(nums: list[int]) -> int:
    return max(nums) - min(nums) if nums else 0
