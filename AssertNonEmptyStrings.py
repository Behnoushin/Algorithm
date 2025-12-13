# - Assert that all strings in the list are non-empty.
# - Time: O(n), Space: O(1)

class Solution:
    def assertNonEmptyStrings(self, strings: list[str]):
        for s in strings:
            assert s != "", "Found an empty string"
