// Average Of Positive Numbers
// - Given a list of numbers, calculate the average of positive numbers only.
// - Example: [3, -2, 5, -1, 4] → 4

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public double AverageOfPositive(List<int> nums)
    {
        var positives = nums.Where(x => x > 0).ToList();

        if (positives.Count == 0)
            return 0;

        return positives.Average();
    }
}
