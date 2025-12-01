# Search First Negative
# - Given a list of integers, return the first negative number.
# - Return None if no negative exists.
# - Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List, Optional

class Solution:
    def searchFirstNegative(self, nums: List[int]) -> Optional[int]:
        for num in nums:
            if num < 0:
                return num
        return None
