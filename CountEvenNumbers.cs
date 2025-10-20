// Count Even Numbers
// - Given a list of integers nums, count how many numbers are even.
// - Return the count as an integer.
// - Time: O(n), Space: O(1)

using System;

public class Solution
{
    public int CountEvenNumbers(int[] nums)
    {
        int count = 0; 

        foreach (int num in nums)
        {
            if (num % 2 == 0) 
            {
                count++; 
            }
        }

        return count; 
    }
}
