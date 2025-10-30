// Sort Numbers in Ascending Order
// - Given a list of integers nums, return the list sorted in ascending order.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> SortAscending(List<int> nums)
    {
        return nums.OrderBy(x => x).ToList();
    }
}
