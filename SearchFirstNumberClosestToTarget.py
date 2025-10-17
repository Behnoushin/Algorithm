# Search First Number Closest to Target
# - Return the number closest to the target.
# - If multiple numbers are equally close, return the first one.
# - Time: O(n), Space: O(1)

class Solution:
    def searchClosestToTarget(self, nums: list[int], target: int) -> int:
        closest = nums[0]
        min_diff = abs(nums[0] - target)
        for x in nums:
            diff = abs(x - target)
            if diff < min_diff:
                closest = x
                min_diff = diff
        return closest
