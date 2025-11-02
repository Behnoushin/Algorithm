# Search Closest To Average
# - Given a list of integers, find the number closest to the average.
# - Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def searchClosestToAverage(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        return min(nums, key=lambda x: abs(x - avg))
