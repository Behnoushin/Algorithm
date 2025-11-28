// Count Strings Containing Digit
// - Given a list of strings, count how many strings contain at least one digit.
// - Time: O(n * m), Space: O(1)

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int CountStringsWithDigit(List<string> strs)
    {
        int count = 0;
        foreach (var s in strs)
        {
            if (s.Any(char.IsDigit))
                count++;
        }
        return count;
    }
}
