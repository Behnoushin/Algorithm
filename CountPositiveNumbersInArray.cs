// Count Positive Numbers in Array
// - Given an array of integers, count how many numbers are positive (> 0).
// - Iterate through the array and increment a counter for each positive number.
// - Time complexity: O(n)
// - Example: [-2, 5, 0, 3, -1, 7, -4] → Output: 3

using System;

class Program
{
    static void Main()
    {
        int[] numbers = { -2, 5, 0, 3, -1, 7, -4 };
        int count = CountPositiveNumbers(numbers);
        Console.WriteLine("Number of positive numbers: " + count);
    }

    static int CountPositiveNumbers(int[] arr)
    {
        int count = 0;

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] > 0)
            {
                count++;
            }
        }

        return count;
    }
}
