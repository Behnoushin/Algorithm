// Capitalize First Letter
// - Capitalize the first letter of each word in a string `s`.

using System;
using System.Globalization;

class Solution
{
    public string CapitalizeFirst(string s)
    {
        TextInfo textInfo = CultureInfo.CurrentCulture.TextInfo;
        return textInfo.ToTitleCase(s.ToLower());
    }
}
