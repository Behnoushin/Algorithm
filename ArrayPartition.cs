// Array Partition
// - Given an integer array `nums` of 2n integers, group the integers into n pairs (a1,b1),(a2,b2),..., (an,bn) 
//   such that the sum of min(ai,bi) is maximized.
// - Return the maximized sum.
// - Constraints:
//   - 1 <= nums.Length <= 2 * 10^4
//   - nums.Length is even
//   - -10^4 <= nums[i] <= 10^4

using System;

public class Solution
{
    public int ArrayPairSum(int[] nums)
    {
        Array.Sort(nums);

        int sum = 0;
        for (int i = 0; i < nums.Length; i += 2)
        {
            sum += nums[i]; 
        }

        return sum;
    }
}
