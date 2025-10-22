// Count Digits
// - Return how many digits a number has.
// - Example: 12345 → 5

using System;

class Solution
{
    public int CountDigits(int num)
    {
        num = Math.Abs(num);

        return num.ToString().Length;
    }
}
