// Reverse Each Word In Sentence
// - Reverse each word in a string `s` while keeping word order.

using System;
using System.Linq;

class Solution
{
    public string ReverseWords(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        var reversedWords = words.Select(word => new string(word.Reverse().ToArray()));
        return string.Join(" ", reversedWords);
    }
}
