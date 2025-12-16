// SumEvenUpToN.cs
// Sum of even numbers from 1 to N

using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number N:");
        int N = Convert.ToInt32(Console.ReadLine());

        int sum = 0;
        for(int i = 2; i <= N; i += 2) 
        {
            sum += i; 
        }

        Console.WriteLine("Sum of even numbers from 1 to " + N + " is: " + sum);
    }
}
