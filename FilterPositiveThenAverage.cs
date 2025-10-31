// FilterPositiveThenAverage
// - Given a list of integers, first filter out only positive numbers.
// - Then calculate and return the average of those positive numbers.
// - If there are no positive numbers, return 0.

using System;
using System.Linq;

class Program
{
    static double FilterPositiveThenAverage(int[] nums)
    {
        var positives = nums.Where(x => x > 0).ToList();
        return positives.Count > 0 ? positives.Average() : 0;
    }
}
