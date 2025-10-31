// Least Common Multiple (LCM)
// - Compute the LCM of two numbers using GCD.

using System;

class Solution
{
    public int LCM(int a, int b)
    {
        return Math.Abs(a * b) / GCD(a, b);
    }

    private int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
