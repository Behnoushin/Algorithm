# - Safely retrieves a nested value from a dictionary.
# - Uses get() to avoid KeyError when intermediate keys are missing.
# - Input: nested dictionary
# - Output: nested value or None
# - Time: O(1), Space: O(1)

class Solution:
    def getNested(self, data: dict):
        user = data.get("user", {})
        return user.get("name")
