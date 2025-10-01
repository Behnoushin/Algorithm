# Contains Duplicate
# - Given an integer array `nums`, return True if any value appears at least twice.
# - Return False if every element is distinct.
# - Constraints:
#   - 1 <= nums.length <= 10^5
#   - -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))