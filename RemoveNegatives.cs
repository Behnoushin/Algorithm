using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> RemoveNegatives(List<int> nums)
    {
        return nums.Where(n => n >= 0).ToList();
    }
}
