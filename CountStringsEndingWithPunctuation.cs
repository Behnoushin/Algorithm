// Count Strings Ending With Punctuation
// - Given a list of strings, count how many strings end with a punctuation mark (.,!?, etc.).
// - Time: O(n), Space: O(1)

using System;
using System.Collections.Generic;

class Solution
{
    public int CountStringsEndingWithPunctuation(List<string> strs)
    {
        int count = 0;
        char[] punctuation = { '.', ',', '!', '?', ';', ':', '-', '"', '\'' };

        foreach (var s in strs)
        {
            if (!string.IsNullOrEmpty(s) && Array.Exists(punctuation, p => p == s[^1]))
            {
                count++;
            }
        }

        return count;
    }
}
