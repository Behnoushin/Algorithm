// Square List
// - Return a new list with each number squared.
// - Example: [1, 2, 3] → [1, 4, 9]

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> SquareList(List<int> nums)
    {
        return nums.Select(x => x * x).ToList();
    }
}
