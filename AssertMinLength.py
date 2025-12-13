# - Assert that all strings have at least min_length characters.
# - Time: O(n), Space: O(1)

class Solution:
    def assertMinLength(self, strings: list[str], min_length: int):
        for s in strings:
            assert len(s) >= min_length, f"String too short: '{s}'"
