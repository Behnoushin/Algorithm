// Sort Numbers in Descending Order
// - Given a list of integers nums, return the list sorted in descending order.
// - Time: O(n log n), Space: O(n)

using System;
using System.Linq;


public class Solution
{
    public int[] SortArrayDescending(int[] nums)
    {
        return nums.OrderByDescending(x => x).ToArray();
    }
}
