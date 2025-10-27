// Temperature Converter
// - Convert temperature between Celsius and Fahrenheit.

using System;

class Solution
{
    // Celsius to Fahrenheit
    public double CelsiusToFahrenheit(double celsius)
    {
        return (celsius * 9.0 / 5.0) + 32.0;
    }

    // Fahrenheit to Celsius
    public double FahrenheitToCelsius(double fahrenheit)
    {
        return (fahrenheit - 32.0) * 5.0 / 9.0;
    }
}
