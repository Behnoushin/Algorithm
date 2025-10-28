// Reverse Array
// - Reverse an integer array manually without using Array.Reverse().
// - Example: [1, 2, 3] → [3, 2, 1]

using System;

class Solution
{
    public int[] ReverseArray(int[] nums)
    {
        int n = nums.Length;
        int[] reversed = new int[n]; 

        for (int i = 0; i < n; i++)
        {
            reversed[i] = nums[n - 1 - i];
        }

        return reversed;
    }
}
