# Find Top K Number
# - Given an integer array `nums` and an integer `k`, find the number that ranks k-th when sorted from largest to smallest.
# - Constraints:
#   - 1 <= k <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def findTopKNumber(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True) 
        return nums[k-1]     
