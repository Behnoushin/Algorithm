// Sort Words by Last Letter
// - Given a list of words, return them sorted by their last character.

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<string> SortByLastLetter(List<string> words)
    {
        return words.OrderBy(w => w[w.Length - 1]).ToList();
    }
}
