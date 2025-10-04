// Check Balanced String
// - Given a string num consisting only of digits.
// - A string is balanced if the sum of digits at even indices equals the sum at odd indices.
// - Return true if balanced, otherwise false.
// - Time: O(n), Space: O(1)

using System;

public class Solution {
    public bool IsBalanced(string num) {
        int evenSum = 0;
        int oddSum = 0;

        for (int i = 0; i < num.Length; i++) {
            int digit = num[i] - '0'; //Convert character to number
            if (i % 2 == 0)
                evenSum += digit;
            else
                oddSum += digit;
        }

        return evenSum == oddSum;
    }
}