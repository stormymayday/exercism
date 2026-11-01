def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    current_total = 1
    for _ in range(2, number + 1):
        current_total *= 2
    return current_total

def total():
    result = 0
    for current_square in range(1, 65):
        result += square(current_square)
    return result
