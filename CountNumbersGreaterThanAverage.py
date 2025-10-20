# Count Numbers Greater Than Average
# - Given an integer array `nums`, count how many numbers are greater than the average of the array.
# - Constraints:
#   - 1 <= nums.length <= 10^4
#   - -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def countAboveAverage(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums) 
        return sum(1 for num in nums if num > avg)  
