# Find Minimum Number in List
# - Given a list of integers nums, return the smallest number.
# - Time: O(n), Space: O(1)

class Solution:
    def findMinimum(self, nums: list[int]) -> int:
        if not nums:
            return None
        minimum = nums[0]
        for num in nums[1:]:
            if num < minimum:
                minimum = num
        return minimum
