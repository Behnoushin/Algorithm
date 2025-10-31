// Filter Positive Numbers
// - Given a list of integers, return only positive numbers.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> FilterPositive(List<int> nums)
    {
        return nums.Where(x => x > 0).ToList();
    }
}
