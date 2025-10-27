# Temperature Converter
# - Convert temperature between Celsius and Fahrenheit.
# - Formulas:
#   - C → F : (C * 9/5) + 32
#   - F → C : (F - 32) * 5/9
# - Constraints:
#   - Temperature values can be any real number.

class Solution:
    def celsiusToFahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32

    def fahrenheitToCelsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9
