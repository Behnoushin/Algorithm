// Sum of Numbers Divisible by K
// - Given a list of integers nums and an integer K,
//   return the sum of numbers divisible by K.

using System;
using System.Collections.Generic;

class Solution
{
    public int SumDivisibleByK(List<int> nums, int K)
    {
        int total = 0;

        foreach (int num in nums)
        {
            if (num % K == 0)
            {
                total += num;
            }
        }

        return total;
    }
}
