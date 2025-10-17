# Filter Positive Numbers
# - Given a list of integers, return only positive numbers.
# - Time: O(n), Space: O(n)

class Solution:
    def filterPositive(self, nums: list[int]) -> list[int]:
        return [x for x in nums if x > 0]
