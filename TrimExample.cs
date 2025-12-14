// Remove extra spaces from start and end of a string

using System;

class Program
{
    static void Main()
    {
        string text = "   Behnoush   ";
        string trimmed = text.Trim(); 

        Console.WriteLine("Original: '" + text + "'");
        Console.WriteLine("Trimmed: '" + trimmed + "'");
    }
}
