# Kth Largest Element
# - Given an integer array `nums` and an integer `k`, return the kth largest element.
# - Constraints:
#   - 1 <= k <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
