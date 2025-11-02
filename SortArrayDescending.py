# Sort Array Descending
# - Given an integer array `nums`, sort it from largest to smallest.
# - Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def sortDescending(self, nums: List[int]) -> List[int]:
        return sorted(nums, reverse=True)
