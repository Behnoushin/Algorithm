// Count Numbers At Even Indices
// - Count how many numbers are at even indices.
// - Example: [1,2,3,4,5] → 3 (indices 0,2,4)

using System;
using System.Collections.Generic;

class Solution
{
    public int CountEvenIndices(List<int> nums)
    {
        int count = 0;

        for (int i = 0; i < nums.Count; i += 2) 
        {
            count++;
        }

        return count;
    }
}
