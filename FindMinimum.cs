// Find Minimum Number in List
// - Given a list of integers nums, return the smallest number.
// - Time: O(n), Space: O(1)

using System;
using System.Collections.Generic;

class Solution
{
    public int? FindMinimum(List<int> nums)
    {
        if (nums == null || nums.Count == 0)
            return null; 

        int minimum = nums[0]; 
        for (int i = 1; i < nums.Count; i++)
        {
            if (nums[i] < minimum)
            {
                minimum = nums[i]; 
            }
        }
        return minimum;
    }
}
