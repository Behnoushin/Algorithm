# Search First Number Divisible by M and Sum of Digits Greater Than K
# - Find the first number divisible by M with digit sum > K.
# - Return None if no such number exists.
# - Time: O(n * log(max_num)), Space: O(1)

class Solution:
    def searchFirstDivisibleByMAndDigitSumGreaterThanK(self, nums: list[int], M: int, K: int) -> int | None:
        for x in nums:
            if x % M == 0 and sum(int(d) for d in str(abs(x))) > K:
                return x
        return None
