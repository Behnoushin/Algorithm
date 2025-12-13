# - Assert that all numbers are within a specified range.
# - Time: O(n), Space: O(1)

class Solution:
    def assertInRange(self, nums: list[int], min_val: int, max_val: int):
        for n in nums:
            assert min_val <= n <= max_val, f"Number {n} out of range [{min_val}, {max_val}]"
