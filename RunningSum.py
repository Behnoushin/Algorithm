# Running Sum
# - Given an array nums, return the running sum of the array.
# - Running sum: runningSum[i] = sum(nums[0]...nums[i])
# - Can be solved iteratively with a single pass.
# - Time: O(n), Space: O(n)

class Solution:
    def runningSum(self, nums):
        res = []
        current_sum = 0
        for num in nums:
            current_sum += num
            res.append(current_sum)
        return res
