# Search First Number Not Divisible by Any in List
# - Find first number that is not divisible by any number in divisors list.
# - Return None if no such number exists.
# - Time: O(n * m), Space: O(1)

class Solution:
    def searchFirstNumberNotDivisibleByList(self, nums: list[int], divisors: list[int]) -> int | None:
        for x in nums:
            if all(x % d != 0 for d in divisors):
                return x
        return None
