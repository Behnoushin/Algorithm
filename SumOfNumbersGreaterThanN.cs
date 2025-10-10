// Sum of Numbers Greater Than N
// - Given a list of integers nums and an integer N,
//   return the sum of numbers greater than N.
// - Time: O(n), Space: O(1)

using System;
using System.Collections.Generic;

public class Solution
{
    public int SumGreaterThanN(List<int> nums, int N)
    {
        int total = 0;
        foreach (int num in nums)
        {
            if (num > N)
            {
                total += num;
            }
        }
        return total;
    }
}
