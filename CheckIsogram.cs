// Check Isogram
// - Determine if a word `s` has no repeating letters.

using System;
using System.Collections.Generic;

class Solution
{
    public bool IsIsogram(string s)
    {
        s = s.ToLower();
        HashSet<char> seen = new HashSet<char>();

        foreach (char c in s)
        {
            if (Char.IsLetter(c))
            {
                if (seen.Contains(c))
                    return false;
                seen.Add(c);
            }
        }

        return true;
    }
}
