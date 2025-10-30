// Sum Squares Positive Greater Than N
// - Given an array of integers and a number N
// - Filter positive numbers greater than N
// - Square each filtered number
// - Return the sum of these squares
// - Example: nums = [1, 3, -2, 5, 7], N = 3 → 5² + 7² = 25 + 49 = 74

using System;

public class Solution
{
    public int SumSquaresPositiveGreaterThanN(int[] nums, int N)
    {
        int sum = 0;
        foreach (int x in nums)
        {
            if (x > N && x > 0)    
            {
                sum += x * x;    
            }
        }
        return sum;
    }
}
