// Assign Cookies
// - Given two integer arrays `g` (children’s greed factors) and `s` (cookie sizes).  
// - Each child can receive at most one cookie.  
// - A child i is content if there exists a cookie j such that `s[j] >= g[i]`.  
// - Return the maximum number of content children.  

using System;

public class Solution
{
    public int FindContentChildren(int[] g, int[] s)
    {
        Array.Sort(g);
        Array.Sort(s);

        int i = 0; 

        foreach (int cookie in s)
        {
            if (i >= g.Length) 
            {
                break;
            }

            if (cookie >= g[i]) 
            {
                i++; 
            }
        }

        return i; 
    }
}
