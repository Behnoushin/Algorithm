# - Unpack a list into a, b, *rest and return sum of all elements.
# - Time: O(n), Space: O(1)

class Solution:
    def unpackAndSum(self, items: list[int]) -> int:
        a, b, *rest = items
        return a + b + sum(rest)