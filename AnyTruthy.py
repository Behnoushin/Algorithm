# - Check if any element in the list is truthy.
# - Time: O(n), Space: O(1)

class Solution:
    def anyTruthy(self, items: list) -> bool:
        return any(items)