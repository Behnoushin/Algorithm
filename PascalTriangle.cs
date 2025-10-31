// Pascal Triangle
// - Generate Pascal's Triangle up to n rows.
// - Each number is the sum of the two numbers directly above it.

using System;
using System.Collections.Generic;

class Solution
{
    public List<List<int>> Generate(int numRows)
    {
        var triangle = new List<List<int>>();

        for (int i = 0; i < numRows; i++)
        {
            var row = new List<int>(new int[i + 1]);
            for (int k = 0; k <= i; k++)
                row[k] = 1;

            for (int j = 1; j < i; j++)
            {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }

            triangle.Add(row);
        }

        return triangle;
    }
}
