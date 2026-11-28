"""Minimal geometry primitives with validated dimensions."""

import math
from dataclasses import dataclass
from numbers import Real


def _require_positive_finite(value, name):
    """Reject non-real, non-finite, zero, and negative dimensions."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a positive finite real number")
    try:
        valid = math.isfinite(value) and value > 0
    except (OverflowError, TypeError, ValueError):
        valid = False
    if not valid:
        raise ValueError(f"{name} must be a positive finite real number")


@dataclass(frozen=True)
class Circle:
    radius: float

    def __post_init__(self):
        _require_positive_finite(self.radius, "radius")

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        _require_positive_finite(self.width, "width")
        _require_positive_finite(self.height, "height")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


@dataclass(frozen=True)
class Triangle:
    a: float
    b: float
    c: float

    def __post_init__(self):
        for name in ("a", "b", "c"):
            _require_positive_finite(getattr(self, name), name)
        if not (
            self.a + self.b > self.c
            and self.a + self.c > self.b
            and self.b + self.c > self.a
        ):
            raise ValueError("triangle sides must satisfy strict triangle inequalities")

    def area(self):
        semiperimeter = self.perimeter() / 2
        heron_product = (
            semiperimeter
            * (semiperimeter - self.a)
            * (semiperimeter - self.b)
            * (semiperimeter - self.c)
        )
        return math.sqrt(max(0.0, heron_product))

    def perimeter(self):
        return self.a + self.b + self.c
