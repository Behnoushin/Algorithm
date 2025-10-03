// Factorial
// - Given an integer n, calculate n! = n * (n-1) * ... * 1
// - 0! = 1 by definition
// - Can be solved recursively or iteratively.

using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter a number: ");
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine($"Factorial of {n} is {Factorial(n)}");
    }

    static int Factorial(int n)
    {
        if (n == 0 || n == 1)
        {
            return 1;
        }
        return n * Factorial(n - 1);
    }
}
