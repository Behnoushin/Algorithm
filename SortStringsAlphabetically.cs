// Sort Strings Alphabetically
// - Given a list of strings, return the list sorted in alphabetical order.
// - Time: O(n log n), Space: O(n)

using System;
using System.Linq;

public class Solution
{
    public string[] SortStringsAlphabetically(string[] words)
    {
        return words.OrderBy(w => w).ToArray();
    }
}
