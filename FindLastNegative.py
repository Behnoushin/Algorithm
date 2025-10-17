# Find Last Negative Number in List
# - Given a list of integers nums, return the last negative number.
# - Time: O(n), Space: O(1)

class Solution:
    def findLastNegative(self, nums: list[int]) -> int:
        last_negative = None
        for num in nums:
            if num < 0:
                last_negative = num
        return last_negative
