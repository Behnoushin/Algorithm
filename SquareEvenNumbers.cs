// SquareEvenNumbers
// - Given a list of integers, return a new list containing only even numbers squared.

using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static List<int> SquareEvenNumbers(int[] nums)
    {
        return nums.Where(x => x % 2 == 0).Select(x => x * x).ToList();
    }
}
