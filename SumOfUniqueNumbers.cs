// Sum of Unique Numbers
// - Given a list of integers nums, return the sum of unique numbers (ignore duplicates).

using System;
using System.Collections.Generic;

class Solution
{
    public int SumUnique(List<int> nums)
    {
        HashSet<int> uniqueNums = new HashSet<int>(nums);

        int total = 0;

        foreach (int num in uniqueNums)
        {
            total += num;
        }

        return total;
    }
}
