"""Calculates grains of wheat doubling on a chessboard."""

def square(number: int) -> int:
    """Calculate the number of grains on a specific chessboard square."""
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    count = 1
    current_square = 1
    while current_square < number:
        count=count*2
        current_square+=1
    return count

def total() -> int:
    """Calculate the total number of grains on the entire chessboard."""
    total_grains = 0
    for square_number in range(1, 65):
        total_grains += square(square_number)
    return total_grains