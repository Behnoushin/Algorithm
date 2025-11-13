// Filter Unique Numbers
// - Given a list of integers, return only numbers that appear once.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> FilterUnique(List<int> nums)
    {
        var counts = new Dictionary<int, int>();

        foreach (var num in nums)
        {
            if (counts.ContainsKey(num))
                counts[num]++;
            else
                counts[num] = 1;
        }

        return nums.Where(x => counts[x] == 1).ToList();
    }
}
