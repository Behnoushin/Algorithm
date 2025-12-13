# - Appends elements to a list only if they are not already present.
# - Demonstrates combining append with conditional checks to avoid duplicates.
# - Time complexity: O(n^2) in worst case due to 'in' check, Space: O(n)
# - Useful for building lists with unique items.

class Solution:
    def appendUnique(self, nums: list[int]) -> list[int]:
        result = []
        for num in nums:
            if num not in result:
                result.append(num)
        return result
