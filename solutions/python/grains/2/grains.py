def square(number: int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    count = 1
    i = 1
    while i < number:
        count=count*2
        i+=1
    return count

def total() -> int:
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum