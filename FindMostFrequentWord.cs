// Find Most Frequent Word
// - Find the word that appears most frequently in a string `s`.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public string MostFrequentWord(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        var counts = new Dictionary<string, int>();

        foreach (var word in words)
        {
            if (counts.ContainsKey(word))
                counts[word]++;
            else
                counts[word] = 1;
        }

        int maxCount = counts.Values.Max();

        foreach (var word in words)
        {
            if (counts[word] == maxCount)
                return word;
        }

        return ""; 
    }
}
