# Search Minimum
# - Given a list of integers, return the smallest value.
# - Time: O(n), Space: O(1)

class Solution:
    def searchMin(self, nums: list[int]) -> int:
        smallest = nums[0]
        for x in nums:
            if x < smallest:
                smallest = x
        return smallest
