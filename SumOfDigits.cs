// Sum of Digits
// - Given an integer n, return the sum of its digits.
// - Example: 123 -> 1 + 2 + 3 = 6
// - Can be solved recursively or using loops.

using System;

class Program
{
    static int SumOfDigits(int n)
    {
        if (n == 0)
            return 0;           
        return (n % 10) + SumOfDigits(n / 10); 
    }

    static void Main()
    {
        Console.Write("Enter a number: ");
        int n = int.Parse(Console.ReadLine());
        int result = SumOfDigits(n);
        Console.WriteLine($"Sum of digits of {n} = {result}");
    }
}
