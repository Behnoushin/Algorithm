// Filter Even Numbers
// - Given a list of integers, return only the even numbers.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> FilterEven(List<int> nums)
    {
        return nums.Where(x => x % 2 == 0).ToList();
    }
}
