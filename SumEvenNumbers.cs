// SumEvenNumbers.cs
// Sum of Even Numbers from 1 to N
// - Calculate the sum of all even numbers between 1 and N
// - Time: O(N), Space: O(1)

using System;

class Solution
{
    public int SumEven(int n)
    {
        int sum = 0; 

        for (int i = 1; i <= n; i++)
        {
            if (i % 2 == 0)
            {
                sum += i; 
            }
        }

        return sum; 
    }
}

class Program
{
    static void Main()
    {
        Solution sol = new Solution();
        int N = 6;
        Console.WriteLine(sol.SumEven(N)); 
    }
}
