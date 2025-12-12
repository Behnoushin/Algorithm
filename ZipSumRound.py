# - Pair numbers with zip, sum them, round results.
# - Time: O(n), Space: O(n)

class Solution:
    def zipSumRound(self, a: list[float], b: list[float]) -> list[float]:
        result = []
        for x, y in zip(a, b):
            result.append(round(x + y, 1))
        return result
