// Length of Last Word
// - Given a string s consisting of words and spaces,
//   return the length of the last word in the string.
// - A word is a maximal substring of non-space characters
// - Spaces at the end of the string should be ignored

using System;

class Solution
{
    public int LengthOfLastWord(string s)
    {
        s = s.Trim();

        string[] words = s.Split(' ');

        return words[words.Length - 1].Length;
    }
}
