# Sort Numbers by Even First
# - Given a list of integers, sort them so that even numbers come before odd numbers.
# - Time: O(n log n), Space: O(n)

class Solution:
    def sortByEvenFirst(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: x % 2)
