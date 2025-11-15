// CountVowelsAndConsonants
// - Given a string s, count vowels and consonants.
// - Return a tuple (vowels_count, consonants_count).
// - Time: O(n), Space: O(1)

using System;

public class Solution {
    public (int, int) CountVowelsAndConsonants(string s) {
        string vowels = "aeiouAEIOU";
        int vCount = 0, cCount = 0;

        foreach (char ch in s) {
            if (char.IsLetter(ch)) {
                if (vowels.Contains(ch)) vCount++;
                else cCount++;
            }
        }

        return (vCount, cCount);
    }
}
