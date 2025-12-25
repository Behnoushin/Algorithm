# - Given a list with mixed data types, sum only the integers.
# - Time: O(n), Space: O(1)

class Solution:
    def sumIntegers(self, items: list) -> int:
        return sum(x for x in items if isinstance(x, int))