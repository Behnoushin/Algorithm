// Count Unique Characters
// - Given a string s, count how many unique characters appear in it.
// - Return the count as an integer.
// - Time: O(n), Space: O(k) where k is the number of unique characters.

using System;
using System.Collections.Generic;

class Program
{
    static int CountUniqueChars(string s)
    {
        HashSet<char> uniqueChars = new HashSet<char>();
        foreach (char ch in s)
        {
            uniqueChars.Add(ch);
        }
        return uniqueChars.Count;
    }

    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();
        int result = CountUniqueChars(input);
        Console.WriteLine($"Number of unique characters: {result}");
    }
}
