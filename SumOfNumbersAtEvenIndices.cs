// Sum of Numbers at Even Indices
// - Given a list of integers nums, return the sum of numbers at even indices (0,2,4,...).

using System;
using System.Collections.Generic;

class Solution
{
    public int SumEvenIndices(List<int> nums)
    {
        int total = 0;

        for (int i = 0; i < nums.Count; i += 2)
        {
            total += nums[i];
        }

        return total;
    }
}
