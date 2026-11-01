"""Collatz Conjecture"""

def steps(number: int) -> int:
    """
    Calculate the number of steps to reach 1 via Collatz Conjecture for a given number

    Parameters:
        number (int): a positive integer

    Returns:
        int: number of steps to reach 1 via Collatz Conjecture for a given number
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    current_number_of_steps = 0
    current_number = number
    
    while current_number != 1:
        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = current_number * 3 + 1

        current_number_of_steps += 1
    
    return current_number_of_steps
