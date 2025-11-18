// Multiply Each Number by 2
// - Given a list of numbers, return a new list where each number is multiplied by 2.
// - Example: [1, 2, 3, 4] → [2, 4, 6, 8]

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> MultiplyByTwo(List<int> nums)
    {
        return nums.Select(x => x * 2).ToList();
    }
}
