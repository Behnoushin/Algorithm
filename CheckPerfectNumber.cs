// Check Perfect Number
// - A perfect number is a number equal to the sum of its proper divisors.
// - Time: O(sqrt(n)), Space: O(1)

using System;

class Solution
{
    public bool CheckPerfectNumber(int n)
    {
        if (n < 2)
            return false;

        int total = 1;

        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                total += i;
                if (i != n / i)
                    total += n / i;
            }
        }

        return total == n;
    }
}
