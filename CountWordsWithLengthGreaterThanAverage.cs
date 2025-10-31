// Count Words With Length Greater Than Average
// - Given a string s containing words separated by spaces,
//   count how many words have length greater than the average length of all words.
// - Return the count as an integer.
// - Time: O(n), Space: O(1)

using System;
using System.Linq;

class Solution
{
    public int CountWordsLongerThanAverage(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (words.Length == 0)
            return 0;

        double averageLength = words.Average(w => w.Length);
        int count = words.Count(w => w.Length > averageLength);

        return count;
    }
}
