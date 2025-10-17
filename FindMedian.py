# Find Median Number in List
# - Given a list of integers nums, return the median value.
# - Time: O(n log n), Space: O(1)

class Solution:
    def findMedian(self, nums: list[int]) -> float:
        if not nums:
            return None
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            return sorted_nums[mid]
