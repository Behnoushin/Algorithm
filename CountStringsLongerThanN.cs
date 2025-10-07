// Count Strings Longer Than N
// - Given a list of strings strs and an integer n,
//   count how many strings have length greater than n.
// - Return the count as an integer.
// - Time: O(n), Space: O(1)

using System;

class Program
{
    static int CountStringsLongerThanN(string[] strs, int n)
    {
        int count = 0;
        foreach (string s in strs)
        {
            if (s.Length > n)
                count++;
        }
        return count;
    }

    static void Main()
    {
        Console.Write("Enter number of strings: ");
        int m = int.Parse(Console.ReadLine());

        string[] strs = new string[m];
        for (int i = 0; i < m; i++)
        {
            Console.Write($"Enter string {i + 1}: ");
            strs[i] = Console.ReadLine();
        }

        Console.Write("Enter integer n: ");
        int n = int.Parse(Console.ReadLine());

        int result = CountStringsLongerThanN(strs, n);
        Console.WriteLine($"Number of strings longer than {n}: {result}");
    }
}
