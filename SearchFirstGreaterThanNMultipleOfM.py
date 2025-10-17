# Search First Number Greater Than N and Multiple of M
# - Given a list of integers, return the first number that is greater than N and divisible by M.
# - Return None if no such number exists.
# - Time: O(n), Space: O(1)

class Solution:
    def searchFirstGreaterThanNMultipleOfM(self, nums: list[int], N: int, M: int) -> int | None:
        for x in nums:
            if x > N and x % M == 0:
                return x
        return None
