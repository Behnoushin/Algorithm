// Sort Numbers by Even First
// - Given a list of integers, sort them so that even numbers come before odd numbers.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<int> SortByEvenFirst(List<int> nums)
    {
        return nums.OrderBy(x => x % 2).ToList();
    }
}
