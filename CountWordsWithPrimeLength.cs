// Count Words With Prime Length
// - Given a string s containing words separated by spaces,
//   count how many words have a length that is a prime number.
// - Return the count as an integer.
// - Time: O(n * sqrt(m)), Space: O(1)

using System;

class Solution
{
    private bool IsPrime(int num)
    {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        for (int i = 3; i * i <= num; i += 2)
        {
            if (num % i == 0)
                return false;
        }
        return true;
    }

    public int CountWordsWithPrimeLength(string s)
    {
        var words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int count = 0;

        foreach (var word in words)
        {
            if (IsPrime(word.Length))
                count++;
        }

        return count;
    }
}
