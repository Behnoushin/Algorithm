// Remove First Element
// - Return the list without the first element.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> RemoveFirstElement(List<int> nums)
    {
        if (nums.Count <= 1)
            return new List<int>();

        return nums.Skip(1).ToList();
    }
}
