// Check Leap Year
// - Given a year, check if it is a leap year.
// - A leap year is divisible by 4, but not by 100, unless also divisible by 400.

using System;

class Solution
{
    public bool IsLeapYear(int year)
    {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}
