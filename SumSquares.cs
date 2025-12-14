// Sum of Squares of First N Numbers
// - Calculate sum of squares from 1 to N
// - Time: O(1) using formula, Space: O(1)

using System;

class Solution
{
    public int SumOfSquares(int n)
    {
        return n * (n + 1) * (2 * n + 1) / 6;
    }
}

class program
{
    static void main()
    {
        Solution sol = new Solution();
        int N = 5;
        Console.WriteLine(sol.SumOfSquares(N));
    }
}