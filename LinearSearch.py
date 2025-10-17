# Linear Search
# - Given a list of integers and a target value, return True if found, else False.
# - Time: O(n), Space: O(1)

class Solution:
    def linearSearch(self, nums: list[int], target: int) -> bool:
        for x in nums:
            if x == target:
                return True
        return False
