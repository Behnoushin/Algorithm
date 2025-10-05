// FizzBuzz
// - Given an integer n, return a list of strings from 1 to n following these rules:
//   - If divisible by 3 and 5, add "FizzBuzz"
//   - If divisible by 3 only, add "Fizz"
//   - If divisible by 5 only, add "Buzz"
//   - Otherwise, add the number as a string
// - Time complexity: O(n)
// - Example: n = 15 → Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int n = 15;
        List<string> result = FizzBuzz(n);

        foreach (string s in result)
        {
            Console.WriteLine(s);
        }
    }

    static List<string> FizzBuzz(int n)
    {
        List<string> result = new List<string>();

        for (int i = 1; i <= n; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                result.Add("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                result.Add("Fizz");
            }
            else if (i % 5 == 0)
            {
                result.Add("Buzz");
            }
            else
            {
                result.Add(i.ToString());
            }
        }

        return result;
    }
}
