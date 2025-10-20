// Count Numbers Greater Than Average
// - Given an array of integers, count how many numbers are greater than the average of the array.
// - First, calculate the sum and average of all elements.
// - Then, iterate through the array and count elements greater than the average.
// - Time complexity: O(n)
// - Example: [2, 5, 8, 3, 7] → Output: 3

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int[] numbers = { 2, 5, 8, 3, 7 };
        int count = CountAboveAverage(numbers);
        Console.WriteLine("Number of elements greater than average: " + count);
    }

    static int CountAboveAverage(int[] arr)
    {
        double average = arr.Average();
        int count = 0;

        foreach (int num in arr)
        {
            if (num > average)
                count++;
        }

        return count;
    }
}
