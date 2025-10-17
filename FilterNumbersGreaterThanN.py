# Filter Numbers Greater Than N
# - Given a list of integers and a number n, return numbers greater than n.
# - Time: O(n), Space: O(n)

class Solution:
    def filterGreaterThanN(self, nums: list[int], n: int) -> list[int]:
        return [x for x in nums if x > n]
