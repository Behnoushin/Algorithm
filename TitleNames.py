# - Given a list of names, convert each name to title case
# - Time: O(n), Space: O(n)

class Solution:
    def titleNames(self, names: list[str]) -> list[str]:
        return [name.title() for name in names]
