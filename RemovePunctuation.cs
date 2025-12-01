// Remove Punctuation
// - Remove all punctuation characters from a string `s`.

using System;
using System.Linq;

class Solution
{
    public string RemovePunctuation(string s)
    {
        return new string(s.Where(c => !char.IsPunctuation(c)).ToArray());
    }
}
