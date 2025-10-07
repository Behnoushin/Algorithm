# Count Strings Longer Than N
# - Given a list of strings strs and an integer n,
#   count how many strings have length greater than n.
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countStringsLongerThanN(self, strs: list[str], n: int) -> int:
        count = 0
        for s in strs:
            if len(s) > n:
                count += 1
        return count
