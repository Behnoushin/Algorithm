// Calculate average of a list of numbers

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int[] numbers = {10, 20, 30, 40, 50};
        double avg = numbers.Average();

        Console.WriteLine("Average: " + avg);
    }
}
