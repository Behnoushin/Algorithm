// Remove Duplicates
// - Remove duplicate elements from a list.
// - Example: [1, 2, 2, 3, 3, 3] → [1, 2, 3]

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> RemoveDuplicates(List<int> nums)
    {
        return nums.Distinct().ToList();
    }
}
