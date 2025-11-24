// Find Max Difference
// - Find the maximum difference between two numbers in a list.
// - Example: [2, 9, 1, 5] → 8

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int FindMaxDifference(List<int> nums)
    {
        if (nums == null || nums.Count == 0)
            return 0;

        int maxNum = nums.Max();
        int minNum = nums.Min();

        return maxNum - minNum;
    }
}
