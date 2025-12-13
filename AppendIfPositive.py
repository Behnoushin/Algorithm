# - Appends only positive numbers from a given list to a new list.
# - Demonstrates using conditional logic with append to selectively build a list.
# - Input: List of integers
# - Output: List containing only positive integers.
# - Time: O(n), Space: O(n)

class Solution:
    def appendPositive(self, nums: list[int]) -> list[int]:
        result = []
        for num in nums:
            if num > 0:
                result.append(num)
        return result
