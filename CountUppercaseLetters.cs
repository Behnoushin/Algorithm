// Count Uppercase Letters
// - Given a string s, count the number of uppercase letters (A–Z).
// - Return the count as an integer.
// - Time: O(n), Space: O(1)

using System;

class Program
{
    static int CountUppercase(string s)
    {
        int count = 0;
        foreach (char ch in s)
        {
            if (char.IsUpper(ch))
            {
                count++;
            }
        }
        return count;
    }

    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();
        int result = CountUppercase(input);
        Console.WriteLine($"Number of uppercase letters: {result}");
    }
}
