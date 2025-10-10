// Sum of List
// - Given a list of numbers, find the sum of all elements.
// - You can use a loop to calculate the sum manually.

using System;
using System.Collections.Generic;

public class Solution
{
    public int SumList(List<int> arr)
    {
        int total = 0;
        foreach (int num in arr)
        {
            total += num;
        }
        return total;
    }
}
