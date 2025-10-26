// Reverse Digits and Sum
// - Reverse the digits of a number and calculate the sum of digits.
// - Time: O(log10(n)), Space: O(1)

using System;

class Solution
{
    public (int reversed, int sum) ReverseDigitsAndSum(int n)
    {
        int original = n;
        int rev = 0;
        int total = 0;

        while (n > 0)
        {
            int digit = n % 10;     
            rev = rev * 10 + digit; 
            total += digit;        
            n /= 10;            
        }

        return (rev, total);
    }
}
