// Sum of Numbers That Are Multiples of 3 or 5
// - Given a list of integers nums,
//   return the sum of numbers that are multiples of 3 or 5.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int SumMultiplesOf3Or5(List<int> nums)
    {
        int total = 0;

        foreach (int num in nums)
        {
            if (num % 3 == 0 || num % 5 == 0)
            {
                total += num;
            }
        }

        return total;
    }
}
