# - Sums all numeric values in a dictionary.
# - Uses items() to explicitly show value extraction.
# - Input: dictionary with numeric values
# - Output: integer sum
# - Time complexity: O(n), Space complexity: O(1)

class Solution:
    def sumValues(self, data: dict[str, int]) -> int:
        total = 0
        for key, value in data.items():
            total += value
        return total
