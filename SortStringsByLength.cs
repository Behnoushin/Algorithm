// Sort Strings By Length
// - Given a list of strings, return the list sorted by their length in ascending order.
// - Time: O(n log n), Space: O(n)

using System;
using System.Linq;

public class Solution
{
    public string[] SortStringsByLength(string[] words)
    {
        return words.OrderBy(w => w.Length).ToArray();
    }
}
