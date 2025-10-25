// Search Closest To Average
// - Given a list of integers, find the number closest to the average.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int SearchClosestToAverage(List<int> nums)
    {
        double avg = nums.Average();

        return nums.OrderBy(x => Math.Abs(x - avg)).First();
    }
}
