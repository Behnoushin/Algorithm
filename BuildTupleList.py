# - Convert a list into list of tuples (index, value)
# - Time: O(n), Space: O(n)

class Solution:
    def toTupleList(self, items: list) -> list[tuple[int, any]]:
        return [(i, val) for i, val in enumerate(items)]