// Count Words
// - Given a string s, count the number of words separated by spaces.
// - A word is defined as a sequence of non-space characters.
// - Return the count as an integer.

using System;

public class Solution
{
    public int CountWords(string s)
    {
        if (string.IsNullOrWhiteSpace(s))
            return 0;

        string[] words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        return words.Length;
    }
}
