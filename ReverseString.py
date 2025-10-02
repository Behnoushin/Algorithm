# Reverse String
# - Given an array of characters `s`, reverse it in-place.
# - Do not return anything. Modify the input array directly.
# - Constraints:
#   - 1 <= s.length <= 10^5
#   - s[i] is a printable ASCII character.
# - Follow-up: Solve it with O(1) extra memory.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left] 
            left += 1
            right -= 1