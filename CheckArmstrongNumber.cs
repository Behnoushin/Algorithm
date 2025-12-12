// Check Armstrong Number
// - Given an integer `num`, check if it is an Armstrong number.
// - An Armstrong number is a number that is equal to the sum of its digits 
//   raised to the power of the number of digits.
// - Example: 153 → 1^3 + 5^3 + 3^3 = 153 → True

using System;
using System.Linq;

class Solution
{
    public bool IsArmstrong(int num)
    {
        var digits = num.ToString().Select(c => int.Parse(c)).ToArray();

        int power = digits.Length;

        int sum = digits.Sum(d => (int)Math.Pow(d, power));

        return sum == num;
    }
}
