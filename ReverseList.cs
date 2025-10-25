// Reverse List
// - Reverse the elements of a list.
// - Time: O(n), Space: O(n)

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> ReverseList(List<int> nums)
    {
        if (nums == null)
            return new List<int>();

        return nums.AsEnumerable().Reverse().ToList();
    }
}
