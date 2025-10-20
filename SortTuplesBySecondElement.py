# Sort Tuples By Second Element
# - Given a list of tuples `pairs`, sort them based on the second element of each tuple.
# - Constraints:
#   - 1 <= len(pairs) <= 10^4

from typing import List, Tuple

class Solution:
    def sortBySecond(self, pairs: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
        return sorted(pairs, key=lambda x: x[1])
