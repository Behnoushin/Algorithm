# - This class provides a method to append a number to an existing list.
# - The append operation adds the number at the end of the list without modifying other elements.
# - This is useful for dynamically building a list while iterating through input numbers.
# - Time complexity: O(1) for each append, total O(n) if appending n elements.
# - Space complexity: O(n) for the resulting list.

class Solution:
    def appendNumber(self, nums: list[int], n: int) -> list[int]:
        nums.append(n)
        return nums
