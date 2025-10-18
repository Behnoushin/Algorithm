// Remove Element
// Given an integer array nums and an integer val,
// remove all occurrences of val in-place.
// - The order of elements may change
// - Return k, the number of elements not equal to val
// - The first k elements of nums should contain the valid elements


using System;

public class Solution
{
    public int RemoveElement(int[] nums, int val)
    {
        int k = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != val)
            {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}
