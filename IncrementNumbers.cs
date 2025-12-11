// Increment Numbers
// - Return a list with each number increased by 1.

using System;
using System.Linq;

class Solution
{
    public int[] IncrementNumbers(int[] nums)
    {
        return nums.Select(x => x + 1).ToArray();
    }
}
