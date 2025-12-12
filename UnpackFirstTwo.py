# - Unpack the first two elements of a list into variables a and b, return as tuple.
# - Time: O(1), Space: O(1)

class Solution:
    def unpackFirstTwo(self, items: list[int]) -> tuple[int, int]:
        a, b, *rest = items
        return a, b