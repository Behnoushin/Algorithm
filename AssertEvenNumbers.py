# - Assert that all numbers in the list are even.
# - Time: O(n), Space: O(1)

class Solution:
    def assertEvenNumbers(self, nums: list[int]):
        for n in nums:
            assert n % 2 == 0, f"Found odd number: {n}"
