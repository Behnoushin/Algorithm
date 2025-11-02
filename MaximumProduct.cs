// Maximum Product of Two Numbers
// - Given an integer array `nums`, find the two numbers whose product is maximized.
// - Return the maximum product.
// - Constraints:
//   - 2 <= nums.Length <= 10^4
//   - -10^4 <= nums[i] <= 10^4

using System;

public class Solution
{
    public int MaxProduct(int[] nums)
    {
        Array.Sort(nums);

        int product1 = nums[nums.Length - 1] * nums[nums.Length - 2];
        int product2 = nums[0] * nums[1];

        return Math.Max(product1, product2); 
    }
}
