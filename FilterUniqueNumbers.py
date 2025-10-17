# Filter Unique Numbers
# - Given a list of integers, return only numbers that appear once.
# - Time: O(n), Space: O(n)

class Solution:
    def filterUnique(self, nums: list[int]) -> list[int]:
        return [x for x in nums if nums.count(x) == 1]
