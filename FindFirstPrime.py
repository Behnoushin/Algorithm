# Find First Prime Number in List
# - Given a list of integers nums, return the first prime number.
# - Time: O(n*sqrt(m)), Space: O(1), m = number value

class Solution:
    def findFirstPrime(self, nums: list[int]) -> int:

        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        for num in nums:
            if is_prime(num):
                return num
        return None
