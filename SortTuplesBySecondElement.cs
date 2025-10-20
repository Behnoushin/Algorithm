// Sort Tuples By Second Element
// - Given a list of tuples, return the list sorted by the second element of each tuple in ascending order.
// - Time: O(n log n), Space: O(n)

using System;
using System.Linq;

public class Solution
{
    public (int, int)[] SortTuplesBySecondElement((int, int)[] tuples)
    {
        return tuples.OrderBy(t => t.Item2).ToArray();
    }
}
