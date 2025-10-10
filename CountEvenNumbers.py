# Count Even Numbers
# - Given a list of integers nums, count how many numbers are even.
# - Return the count as an integer.
# - Time: O(n), Space: O(1)

class Solution:
    def countEvenNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if num % 2 == 0:
                count += 1
        return count
