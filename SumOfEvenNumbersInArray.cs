// Sum of Even Numbers in Array
// - Given an array of integers, calculate and return the sum of all even numbers.
// - Iterate through the array, check if each element is even (num % 2 == 0).
// - Add even numbers to a running total.
// - Time complexity: O(n)
// - Example: [3, 8, 5, 12, 7, 4, 9, 6] → Output: 30

using System;

class Program
{
    static void Main()
    {
        int[] numbers = { 3, 8, 5, 12, 7, 4, 9, 6 };
        int sum = SumEvenNumbers(numbers);
        Console.WriteLine("Sum of even numbers: " + sum);
    }

    static int SumEvenNumbers(int[] arr)
    {
        int sum = 0;

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] % 2 == 0)
            {
                sum += arr[i];
            }
        }

        return sum;
    }
}
