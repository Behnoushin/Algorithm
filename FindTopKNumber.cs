// Find Top K Number
// - Given an integer array `nums` and an integer `k`, find the number that ranks k-th when sorted from largest to smallest.
// - Constraints:
//   - 1 <= k <= nums.Length <= 10^4
//   - -10^4 <= nums[i] <= 10^4

using System;
public class Solution
{
    public int FindTopKNumber(int[] nums, int k)
    {
        Array.Sort(nums);
        Array.Reverse(nums);

        return nums[k - 1];
    }
}
