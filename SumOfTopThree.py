# Sum of Top Three
# Given a list nums, return the sum of the 3 largest numbers.

class Solution:
    def sumTopThree(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return sum(nums[:3])
