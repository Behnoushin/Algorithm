// Filter Words Starting With Vowel
// - Given a list of words, return only those that start with a vowel.
// - Time: O(n), Space: O(n)

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public List<string> FilterStartingWithVowel(List<string> words)
    {
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u', 
                                                   'A', 'E', 'I', 'O', 'U' };

        return words.Where(w => !string.IsNullOrEmpty(w) && vowels.Contains(w[0])).ToList();
    }
}
