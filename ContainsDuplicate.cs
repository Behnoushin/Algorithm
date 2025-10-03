// Contains Duplicate
// - Given an integer array 'nums', return true if any value appears at least twice.
// - Return false if every element is distinct.
// - Constraints:
//   - 1 <= nums.Length <= 100000
//   - -10^9 <= nums[i] <= 10^9

using System;
using System.Collections.Generic;

class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        HashSet<int> seen = new HashSet<int>();
        
        foreach (int num in nums)
        {
            if (seen.Contains(num))
            {
                return true; 
            }
            seen.Add(num);
        }

        return false; 
    }
}
