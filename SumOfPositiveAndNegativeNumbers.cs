// Sum of Positive and Negative Numbers
// - Given an array of integers, calculate the sum of positive numbers and the sum of negative numbers separately.
// - Iterate through the array, adding each number to the respective sum based on its sign.
// - Time complexity: O(n)
// - Example: [-3, 5, -2, 7, 0, -1, 4] → Output: Positive Sum: 16, Negative Sum: -6

using System;

class Program
{
    static void Main()
    {
        int[] numbers = { -3, 5, -2, 7, 0, -1, 4 };
        int positiveSum = 0;
        int negativeSum = 0;

        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] > 0)
                positiveSum += numbers[i];
            else if (numbers[i] < 0)
                negativeSum += numbers[i];
        }

        Console.WriteLine("Sum of positive numbers: " + positiveSum);
        Console.WriteLine("Sum of negative numbers: " + negativeSum);
    }
}
