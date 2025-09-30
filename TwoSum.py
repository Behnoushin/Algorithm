# Two Sum
# Given an array of integers (nums) and an integer (target),
# return the indices of the two numbers such that they add up to target.
# - Each input has exactly one solution
# - You cannot use the same element twice
# - The answer can be returned in any order

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
