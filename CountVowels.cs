// Count Vowels
// - Given a string s, count the number of vowels (a, e, i, o, u, case-insensitive).
// - Return the count as integer.
// - Time: O(n), Space: O(1)

using System;

public class Solution {
    public int CountVowels(string s) {
        string vowels = "aeiouAEIOU"; 
        int count = 0;

        foreach (char ch in s) {
            if (vowels.Contains(ch)) {
                count++; 
            }
        }

        return count;
    }
}
