# Sum of Triplets
# - Sum the corresponding elements of three lists.
# - Time: O(n), Space: O(n)

class Solution:
    def sumTriplets(self, list1: list[int], list2: list[int], list3: list[int]) -> list[int]:
        return [a + b + c for a, b, c in zip(list1, list2, list3)]
