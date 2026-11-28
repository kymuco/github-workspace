"""Immutable two-dimensional vectors with finite real coordinates."""

from dataclasses import dataclass
import math
from numbers import Real


def _finite_real(value, name):
    """Convert a finite real number to float, rejecting invalid inputs."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a finite real number")
    try:
        number = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite real number") from exc
    if not math.isfinite(number):
        raise ValueError(f"{name} must be a finite real number")
    return number


@dataclass(frozen=True)
class Vector2:
    """A two-dimensional vector; arithmetic returns new vectors."""

    x: float
    y: float

    def __post_init__(self):
        object.__setattr__(self, "x", _finite_real(self.x, "x"))
        object.__setattr__(self, "y", _finite_real(self.y, "y"))

    def __add__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("addition requires another Vector2")
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("subtraction requires another Vector2")
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        factor = _finite_real(scalar, "scalar")
        return Vector2(self.x * factor, self.y * factor)

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        divisor = _finite_real(scalar, "scalar")
        if divisor == 0:
            raise ZeroDivisionError("cannot divide a vector by zero")
        return Vector2(self.x / divisor, self.y / divisor)

    def dot(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("dot product requires another Vector2")
        return self.x * other.x + self.y * other.y

    def length(self):
        return math.hypot(self.x, self.y)

    def distance_to(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("distance requires another Vector2")
        return math.hypot(self.x - other.x, self.y - other.y)

    def normalized(self):
        magnitude = self.length()
        if magnitude == 0:
            raise ValueError("cannot normalize the zero vector")
        return self / magnitude
