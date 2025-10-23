# Count Numbers At Even Indices
# - Count how many numbers are at even indices.
# - Example: [1,2,3,4,5] → 3 (indices 0,2,4)

def countEvenIndices(nums: list[int]) -> int:
    return len(nums[::2])
