// Average Of Even Numbers
// - Given a list of numbers, calculate the average of even numbers only.
// - Example: [1, 2, 3, 4, 5, 6] → 4

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public double AverageOfEvens(List<int> nums)
    {
        var evens = nums.Where(x => x % 2 == 0).ToList();

        if (evens.Count == 0)
            return 0;

        return evens.Average();
    }
}
