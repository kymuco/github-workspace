import math


def circle_area(radius):
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * radius ** 2


def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height
