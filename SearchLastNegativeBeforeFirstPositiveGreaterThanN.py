# Search Last Negative Before First Positive Greater Than N
# - Find the last negative number before the first positive number greater than N.
# - Return None if no such number exists.
# - Time: O(n), Space: O(1)

class Solution:
    def searchLastNegativeBeforeFirstPositiveGreaterThanN(self, nums: list[int], N: int) -> int | None:
        last_negative = None
        for x in nums:
            if x > N:
                break
            if x < 0:
                last_negative = x
        return last_negative
