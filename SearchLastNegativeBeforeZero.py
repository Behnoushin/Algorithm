# Search Last Negative Number Before First Zero
# - Given a list of integers, return the last negative number that appears before the first zero.
# - Return None if no such number exists.
# - Time: O(n), Space: O(1)

class Solution:
    def searchLastNegativeBeforeZero(self, nums: list[int]) -> int | None:
        last_negative = None
        for x in nums:
            if x == 0:
                break
            if x < 0:
                last_negative = x
        return last_negative
