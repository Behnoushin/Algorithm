# Sum Even Numbers
# Given a list containing mixed data types,
# return the sum of all even integers.

class Solution:
    def sumEven(self, nums: list) -> int:
        evens = filter(lambda x: isinstance(x, int) and x % 2 == 0, nums)
        return sum(evens)
