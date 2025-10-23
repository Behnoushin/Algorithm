# Count Digits
# - Return how many digits a number has.
# - Example: 12345 → 5

def countDigits(num: int) -> int:
    return len(str(abs(num)))
