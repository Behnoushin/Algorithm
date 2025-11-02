# Maximum Product of Two Numbers
# - Given an integer array `nums`, find the two numbers whose product is maximized.
# - Return the maximum product.
# - Constraints:
#   - 2 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2], nums[0]*nums[1])
