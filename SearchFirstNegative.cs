// Search First Negative
// - Given a list of integers, return the first negative number.
// - Return null if no negative exists.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int? SearchFirstNegative(List<int> nums)
    {
        foreach (int num in nums)
        {
            if (num < 0)
                return num;
        }
        return null;
    }
}
