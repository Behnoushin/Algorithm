// Average Of List
// - Given a list of numbers, calculate and return their average value.
// - Example: [2, 4, 6, 8] → 5

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public double AverageOfList(List<double> nums)
    {
        if (nums == null || nums.Count == 0)
            return 0;

        return nums.Average();
    }
}
