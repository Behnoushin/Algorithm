// Count Zeros
// - Count how many zeros are in a list.
// - Example: [0,1,0,2] → 2

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int CountZeros(List<int> nums)
    {
        return nums.Count(x => x == 0);
    }
}
