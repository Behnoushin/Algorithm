// Filter Numbers Greater Than N
// - Given a list of integers and a number n, return numbers greater than n.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> FilterGreaterThanN(List<int> nums, int n)
    {
        return nums.Where(x => x > n).ToList();
    }
}
