// Count Words With Only Letters
// - Given a string s containing words separated by spaces,
//   count how many words contain only alphabetic letters (a-z, A-Z).
// - Return the count as an integer.
// - Time: O(n * m), Space: O(1)

using System;
using System.Linq;

class Solution
{
    public int CountWordsWithOnlyLetters(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int count = 0;

        foreach (var word in words)
        {
            if (word.All(char.IsLetter))
                count++;
        }

        return count;
    }
}
