// Search Words With Most Vowels
// - Return the word with the highest number of vowels.
// - If multiple words have same max vowels, return the first one.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public string SearchWordWithMostVowels(List<string> words)
    {
        HashSet<char> vowels = new HashSet<char>{'a','e','i','o','u','A','E','I','O','U'};
        int maxCount = -1;
        string result = "";

        foreach (var w in words)
        {
            int count = w.Count(ch => vowels.Contains(ch));

            if (count > maxCount)
            {
                maxCount = count;
                result = w;
            }
        }

        return result;
    }
}
