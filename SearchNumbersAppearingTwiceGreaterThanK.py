# Search Numbers Appearing Twice and Greater Than K
# - Return all numbers that appear exactly twice and are greater than K.
# - Time: O(n), Space: O(n)

class Solution:
    def searchNumbersAppearingTwiceGreaterThanK(self, nums: list[int], K: int) -> list[int]:
        from collections import Counter
        counter = Counter(nums)
        return [num for num, count in counter.items() if count == 2 and num > K]
