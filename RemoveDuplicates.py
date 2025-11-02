# Remove Duplicates
# - Remove duplicate elements from a list.
# - Example: [1, 2, 2, 3, 3, 3] → [1, 2, 3]

def removeDuplicates(nums: list[int]) -> list[int]:
    return list(set(nums))
