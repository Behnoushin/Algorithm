# - Check if all elements in the list are truthy.
# - Time: O(n), Space: O(1)

class Solution:
    def allTruthy(self, items: list) -> bool:
        return all(items)