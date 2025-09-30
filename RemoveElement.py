# Remove Element
# Given an integer array nums and an integer val,
# remove all occurrences of val in-place.
# - The order of elements may change
# - Return k, the number of elements not equal to val
# - The first k elements of nums should contain the valid elements

def removeElement(nums, val):
    k = 0  
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
