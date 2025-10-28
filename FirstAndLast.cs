// First And Last
// - Return a list containing only the first and last elements of a list.
// - Example: [1,2,3,4] → [1,4]

using System;
using System.Collections.Generic;

class Solution
{
    public List<int> FirstAndLast(List<int> nums)
    {
        if (nums == null || nums.Count == 0)
            return new List<int>();

        return new List<int> { nums[0], nums[nums.Count - 1] };
    }
}
