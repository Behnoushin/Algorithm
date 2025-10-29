// Find Min-Max Difference
// - Return difference between largest and smallest number in a list.
// - Example: [3,7,2,5] → 5

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int FindMinMaxDifference(List<int> nums)
    {
        if (nums == null || nums.Count == 0)
            return 0;

        int maxNum = nums.Max();
        int minNum = nums.Min();

        return maxNum - minNum;
    }
}
