// Count Words Starting With Vowel
// - Given a string s containing words separated by spaces,
//   count how many words start with a vowel (a, e, i, o, u), case-insensitive.
// - Time: O(n), Space: O(1)

using System;
using System.Linq;

class Solution
{
    public int CountWordsStartingWithVowel(string s)
    {
        string vowels = "aeiou";
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int count = 0;

        foreach (var word in words)
        {
            char first = char.ToLower(word[0]);
            if (vowels.Contains(first))
            {
                count++;
            }
        }

        return count;
    }
}
