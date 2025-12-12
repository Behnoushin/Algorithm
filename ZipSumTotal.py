# - Sum pairs with zip, round results, calculate total.
# - Time: O(n), Space: O(n)

class Solution:
    def zipSumTotal(self, a: list[float], b: list[float]):
        sums = [round(x+y, 1) for x,y in zip(a,b)]
        total = round(sum(sums), 1)
        return sums, total
