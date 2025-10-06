// Fibonacci
// - Given an integer n, return the nth Fibonacci number.
// - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
// - Can be solved recursively or iteratively.

using System;

class Program
{
    static int Fibonacci(int n)
    {
        if (n == 0)
            return 0;          
        else if (n == 1)
            return 1;       
        else
            return Fibonacci(n - 1) + Fibonacci(n - 2);  
    }

    static void Main()
    {
        Console.Write("Enter n: ");
        int n = int.Parse(Console.ReadLine());
        int result = Fibonacci(n);
        Console.WriteLine($"Fibonacci({n}) = {result}");
    }
}
