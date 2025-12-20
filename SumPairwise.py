# Sum Pairwise
# - Sum the corresponding elements of two lists.
# - Time: O(n), Space: O(n)

class Solution:
    def sumPairwise(self, list1: list[int], list2: list[int]) -> list[int]:
        return [a + b for a, b in zip(list1, list2)]
