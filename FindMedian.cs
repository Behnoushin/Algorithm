// Find Median Number in List
// - Given a list of integers nums, return the median value.
// - Time: O(n log n), Space: O(1)

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public double? FindMedian(List<int> nums)
    {
        if (nums == null || nums.Count == 0)
            return null; 

        nums.Sort(); 

        int n = nums.Count;
        int mid = n / 2;

        if (n % 2 == 0)
        {
            return (nums[mid - 1] + nums[mid]) / 2.0;
        }
        else
        {
            return nums[mid];
        }
    }
}
