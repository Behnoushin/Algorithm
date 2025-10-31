# Pascal Triangle
# - Generate Pascal's Triangle up to n rows.
# - Each number is the sum of the two numbers directly above it.
# - Constraints:
#   - 1 <= numRows <= 30

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
