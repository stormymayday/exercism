"""Module to calculate the number of steps in the Collatz Conjecture."""

def steps(number: int) -> int:
    """Calculate the number of steps to reach 1 using the Collatz Conjecture.

    Args:
        number (int): A positive integer to start the sequence.

    Raises:
        ValueError: If the input number is less than or equal to zero.

    Returns:
        int: The total number of steps taken to reach 1.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        step_count += 1
        
    return step_count