# Height Checker
# - Given an integer array `heights` representing students' current standing order,
#   return the number of indices where the current height differs from the expected
#   height when students are sorted in non-decreasing order.
# - Constraints:
#   - 1 <= heights.length <= 100
#   - 1 <= heights[i] <= 100

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
