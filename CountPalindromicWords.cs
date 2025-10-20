// Count Palindromic Words
// - Given a string s containing words separated by spaces,
//   count how many words are palindromes (words that read the same forward and backward, case-insensitive).
// - Return the count as an integer.
// - Time: O(n * m), Space: O(1) where n is number of words, m is average word length

using System;

public class Solution
{
    public int CountPalindromicWords(string s)
    {
        string[] words = s.Split(' '); 
        int count = 0; 

        foreach (string word in words)
        {
            string cleaned = word.ToLower(); 
            char[] arr = cleaned.ToCharArray();
            Array.Reverse(arr);
            string reversed = new string(arr);

            if (cleaned == reversed) 
            {
                count++; 
            }
        }

        return count; 
    }
}
