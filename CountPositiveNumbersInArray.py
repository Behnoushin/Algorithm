# Count Positive Numbers in Array
# - Given an integer array `nums`, count how many numbers are positive (>0).
# - Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def countPositive(self, nums: List[int]) -> int:
        return sum(1 for num in nums if num > 0)
