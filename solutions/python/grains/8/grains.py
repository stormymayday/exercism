"""Calculate the number of grains of wheat on a chessboard"""

square_map = { 1: 1 }
TOTAL_NUMBER_OF_GRAINS = None

def square(number):
    """Calculate the number of grains on a given square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    if number not in square_map:
        current_total = 1
        for current_square in range(2, number + 1):
            current_total *= 2
            if current_square not in square_map:
                square_map[current_square] = current_total
        return current_total
    else:
        return square_map[number]

def total():
    """Calculate the total number of grains on the chessboard"""
    global TOTAL_NUMBER_OF_GRAINS
    if TOTAL_NUMBER_OF_GRAINS is None:
        current_total = 0
        for current_square in range(1, 65):
            current_total += square(current_square)
        TOTAL_NUMBER_OF_GRAINS = current_total
        return TOTAL_NUMBER_OF_GRAINS
    else:
        return TOTAL_NUMBER_OF_GRAINS
