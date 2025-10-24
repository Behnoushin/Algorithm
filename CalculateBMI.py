# Calculate BMI
# - Given weight (kg) and height (m), calculate the Body Mass Index.
# - Formula: BMI = weight / (height * height)
# - Constraints:
#   - 0 < weight <= 500
#   - 0 < height <= 3

class Solution:
    def calculateBMI(self, weight: float, height: float) -> float:
        return round(weight / (height ** 2), 2)
