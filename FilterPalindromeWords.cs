// Filter Palindrome Words
// - Given a list of words, return only palindrome words.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<string> FilterPalindromes(List<string> words)
    {
        return words.Where(w => w.ToLower() == new string(w.ToLower().Reverse().ToArray())).ToList();
    }
}
