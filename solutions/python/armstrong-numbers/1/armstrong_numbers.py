"""Module to check if a number is an Armstrong number."""

def is_armstrong_number(number: int) -> bool:
    """Determine whether a number is an Armstrong number.

    An Armstrong number equals the sum of its own digits, each raised 
    to the power of the total number of digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to easily work with characters
    string_number = str(number)
    number_of_digits = len(string_number)
    
    total_sum = 0
    for digit_char in string_number:
        # Convert character back to integer and raise to the power of total digits
        total_sum += int(digit_char) ** number_of_digits
    return number == total_sum
