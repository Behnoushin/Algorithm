// Count Consonants
// - Given a string `s`, count all consonant letters.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int CountConsonants(string s)
    {
        string vowels = "aeiouAEIOU";
        return s.Count(c => Char.IsLetter(c) && !vowels.Contains(c));
    }
}
