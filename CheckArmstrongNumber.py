# Check Armstrong Number
# - Given an integer `num`, check if it is an Armstrong number.
# - An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
# - Example: 153 → 1^3 + 5^3 + 3^3 = 153 → True

class Solution:
    def isArmstrong(self, num: int) -> bool:
        digits = [int(d) for d in str(num)]
        power = len(digits)
        return sum(d**power for d in digits) == num
