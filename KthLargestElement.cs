// Kth Largest Element
// - Given an integer array `nums` and an integer `k`, return the kth largest element.
// - Constraints:
//   - 1 <= k <= nums.Length <= 10^4
//   - -10^4 <= nums[i] <= 10^4

using System;

public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        Array.Sort(nums);

        return nums[nums.Length - k];
    }
}
