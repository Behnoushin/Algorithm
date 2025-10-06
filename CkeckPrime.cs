// Check Prime
// - Given an integer n, determine if it is prime.
// - A prime number has no divisors other than 1 and itself.
// - Iterative solution is more efficient than recursive here.

using System;

class Program
{
    static bool IsPrime(int n)
    {
        if (n <= 1)
            return false; 

        for (int i = 2; i <= Math.Sqrt(n); i++)
        {
            if (n % i == 0)
                return false;  
        }

        return true;  
    }

    static void Main()
    {
        Console.Write("Enter a number: ");
        int n = int.Parse(Console.ReadLine());

        if (IsPrime(n))
            Console.WriteLine($"{n} is prime.");
        else
            Console.WriteLine($"{n} is not prime.");
    }
}
