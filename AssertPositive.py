# - Assert that all numbers in the list are positive.
# - Time: O(n), Space: O(1)

class Solution:
    def assertPositive(self, nums: list[int]):
        for n in nums:
            assert n > 0, f"Found non-positive number: {n}"