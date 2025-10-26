// Decrement Numbers
// - Return a list with each number decreased by 1.
// - Example: [1,2,3] → [0,1,2]

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> DecrementNumbers(List<int> nums)
    {
        return nums.Select(x => x - 1).ToList();
    }
}
