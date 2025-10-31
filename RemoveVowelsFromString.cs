// Remove Vowels From String
// - Given a string `s`, remove all vowels (a, e, i, o, u, both cases).

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public string RemoveVowels(string s)
    {
        string vowels = "aeiouAEIOU";
        return new string(s.Where(c => !vowels.Contains(c)).ToArray());
    }
}
