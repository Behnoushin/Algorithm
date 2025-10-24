// Calculate BMI
// - Given weight (kg) and height (m), calculate the Body Mass Index.
// - Formula: BMI = weight / (height * height)

using System;

class Solution
{
    public double CalculateBMI(double weight, double height)
    {
        return Math.Round(weight / (height * height), 2);
    }
}
