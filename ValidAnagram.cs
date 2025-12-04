// Valid Anagram
// Given two strings s and t, return true if t is an anagram of s, otherwise false.
// - An anagram means t has exactly the same letters as s, just rearranged.

using System;
using System.Collections.Generic;

class Solution
{
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length)
            return false;

        var countS = new Dictionary<char, int>();
        var countT = new Dictionary<char, int>();

        foreach (char c in s)
        {
            if (countS.ContainsKey(c))
                countS[c]++;
            else
                countS[c] = 1;
        }

        foreach (char c in t)
        {
            if (countT.ContainsKey(c))
                countT[c]++;
            else
                countT[c] = 1;
        }

        foreach (var kvp in countS)
        {
            if (!countT.ContainsKey(kvp.Key) || countT[kvp.Key] != kvp.Value)
                return false;
        }

        return true;
    }
}
