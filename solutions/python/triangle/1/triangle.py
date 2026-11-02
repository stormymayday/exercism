"""Functions to determine if a triangle is equilateral, isosceles, or scalene."""

def is_triangle(sides: list[int]) -> bool:
    """
    For a shape to be a triangle at all
    - all sides have to be of length > 0
    - the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
    """
    return (
        len(sides) == 3 and
        (
            sides[0] > 0 and
            sides[1] > 0 and
            sides[2] > 0
        ) and
        (
            (sides[0] + sides[1] >= sides[2]) and
            (sides[0] + sides[2] >= sides[1]) and
            (sides[1] + sides[2] >= sides[0])
        )
    )

def equilateral(sides: list[int]) -> bool:
    """An equilateral triangle has all three sides the same length."""

    if not is_triangle(sides):
        return False

    return sides[0] == sides[1] and sides[0] == sides[2]


def isosceles(sides: list[int]) -> bool:
    """An isosceles triangle has at least two sides the same length."""
    pass

    if not is_triangle(sides):
        return False

    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides: list[int]) -> bool:
    """A scalene triangle has all sides of different lengths."""

    if not is_triangle(sides):
        return False

    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
