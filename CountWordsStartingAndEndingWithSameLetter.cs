// Count Words Starting And Ending With Same Letter
// - Given a string s containing words separated by spaces,
//   count how many words start and end with the same letter (case-insensitive).
// - Time: O(n), Space: O(1)

using System;
using System.Linq;

class Solution
{
    public int CountWordsSameStartEnd(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int count = 0;

        foreach (var word in words)
        {
            string lower = word.ToLower();
            if (lower[0] == lower[^1])
            {
                count++;
            }
        }

        return count;
    }
}
