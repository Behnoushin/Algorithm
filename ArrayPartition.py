# Array Partition
# - Given an integer array `nums` of 2n integers, group the integers into n pairs (a1,b1),(a2,b2),..., (an,bn) such that the sum of min(ai,bi) is maximized.
# - Return the maximized sum.
# - Constraints:
#   - 1 <= nums.length <= 2 * 10^4
#   - nums.length is even
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])