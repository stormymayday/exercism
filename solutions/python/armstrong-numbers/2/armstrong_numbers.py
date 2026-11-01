"""
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
"""

def is_armstrong_number(number: int) -> bool:
    """Determine whether a number is an Armstrong number"""
    string_digits = str(number)
    current_sum = 0
    n = len(string_digits)
    for digit in string_digits:
        current_sum += int(digit) ** n

    return number == current_sum