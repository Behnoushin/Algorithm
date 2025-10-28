# First And Last
# - Return a list containing only the first and last elements of a list.
# - Example: [1,2,3,4] → [1,4]

def firstAndLast(nums: list[int]) -> list[int]:
    if not nums:
        return []
    return [nums[0], nums[-1]]
