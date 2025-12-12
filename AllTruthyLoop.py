# - Check if all elements in the list are truthy using a loop.
# - Time: O(n), Space: O(1)

class Solution:
    def allTruthyLoop(self, items: list) -> bool:
        for item in items:
            if not item:
                return False
        return True
