// Sort Strings By Last Character
// - Given a list of strings, return the list sorted by the last character of each string in ascending order.
// - Time: O(n log n), Space: O(n)

using System;
using System.Linq;

public class Solution
{
    public string[] SortStringsByLastCharacter(string[] words)
    {
        return words.OrderBy(w => w[w.Length - 1]).ToArray();
    }
}
