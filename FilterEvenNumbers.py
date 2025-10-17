# Filter Even Numbers
# - Given a list of integers, return only the even numbers.
# - Time: O(n), Space: O(n)

class Solution:
    def filterEven(self, nums: list[int]) -> list[int]:
        return [x for x in nums if x % 2 == 0]
