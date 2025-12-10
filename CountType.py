# - Count how many elements of a given type are in the list.
# - Time: O(n), Space: O(1)

class Solution:
    def countType(self, items: list, t: type) -> int:
        return sum(1 for x in items if isinstance(x, t))