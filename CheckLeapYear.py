# Check Leap Year
# - Given a year, check if it is a leap year.
# - A leap year is divisible by 4, but not by 100, unless also divisible by 400.
# - Constraints:
#   - 1 <= year <= 10^6

class Solution:
    def isLeapYear(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
