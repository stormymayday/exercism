"""Calculates grains of wheat doubling on a chessboard."""

def square(number: int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    count = 1
    current_square = 1
    while current_square < number:
        count=count*2
        current_square+=1
    return count

def total() -> int:
    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains