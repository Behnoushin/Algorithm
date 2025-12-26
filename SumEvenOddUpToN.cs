// Sum of even and odd numbers up to N

using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number N:");
        int N = Convert.ToInt32(Console.ReadLine());

        int sumEven = 0;
        int sumOdd = 0;

        for(int i = 1; i <= N; i++) 
        {
            if(i % 2 == 0)
            {
                sumEven += i; 
            }
            else
            {
                sumOdd += i; 
            }
        }

        Console.WriteLine("Sum of even numbers: " + sumEven);
        Console.WriteLine("Sum of odd numbers: " + sumOdd);
    }
}
