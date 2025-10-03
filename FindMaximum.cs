// Find Maximum
// - Given an array of integers, find the maximum value.
// - You can use the built-in methods or implement it manually with a loop.

using System;

class Program
{
    static void Main(string[] args)
    {
        int[] nums = {3, 7, 2, 10, 4};  
        int maximum = nums[0];       

        for (int i = 1; i < nums.Length; i++)  
        {
            if (nums[i] > maximum)          
            {
                maximum = nums[i];           
            }
        }

        Console.WriteLine($"Maximum value is: {maximum}");
    }
}
