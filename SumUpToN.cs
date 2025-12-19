// SumUpToN.cs
// Sum of numbers from 1 to N

using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number N:");
        int N = Convert.ToInt32(Console.ReadLine());

        int sum = 0;
        for(int i = 1; i <= N; i++) 
        {
            sum += i;
        }

        Console.WriteLine("Sum of numbers from 1 to " + N + " is: " + sum);
    }
}
