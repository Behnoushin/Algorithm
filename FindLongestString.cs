// Find Longest String in List
// - Given a list of strings strs, return the longest string.
// - Time: O(n), Space: O(1)

using System;
using System.Collections.Generic;

class Solution
{
    public string FindLongestString(List<string> strs)
    {
        if (strs == null || strs.Count == 0)
            return "";

        string longest = strs[0];

        foreach (var s in strs)
        {
            if (s.Length > longest.Length)
            {
                longest = s;
            }
        }

        return longest;
    }
}
