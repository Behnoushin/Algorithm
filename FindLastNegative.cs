// Find Last Negative Number in List
// - Given a list of integers nums, return the last negative number.
// - Time: O(n), Space: O(1)

using System;
using System.Collections.Generic;

class Solution
{
    public int? FindLastNegative(List<int> nums)
    {
        int? lastNegative = null;

        foreach (var num in nums)
        {
            if (num < 0)
            {
                lastNegative = num;
            }
        }

        return lastNegative;
    }
}
