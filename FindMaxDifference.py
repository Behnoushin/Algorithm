# Find Max Difference
# - Find the maximum difference between two numbers in a list.
# - Example: [2, 9, 1, 5] → 8

def findMaxDifference(nums: list[int]) -> int:
    if not nums:
        return 0
    return max(nums) - min(nums)
