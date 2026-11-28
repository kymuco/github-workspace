"""Small immutable linear algebra primitives (standard library only)."""

from dataclasses import dataclass
import math
from numbers import Real


def _finite_number(value, label):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{label} must be a real number")
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{label} is outside the finite floating-point range") from exc
    if not math.isfinite(number):
        raise ValueError(f"{label} must be finite")
    return number


def _items(values, label):
    if isinstance(values, (str, bytes)):
        raise TypeError(f"{label} must be an iterable of numbers")
    try:
        return tuple(values)
    except TypeError as exc:
        raise TypeError(f"{label} must be an iterable of numbers") from exc


@dataclass(frozen=True, init=False)
class Vector:
    """A vector of one or more finite real components."""

    values: tuple

    def __init__(self, values):
        components = _items(values, "vector")
        if not components:
            raise ValueError("vector dimension must be positive")
        object.__setattr__(
            self, "values",
            tuple(_finite_number(value, "vector component") for value in components),
        )

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("vector addition requires another Vector")
        if len(self) != len(other):
            raise ValueError("vector dimensions must match")
        return Vector(a + b for a, b in zip(self.values, other.values))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("vector subtraction requires another Vector")
        if len(self) != len(other):
            raise ValueError("vector dimensions must match")
        return Vector(a - b for a, b in zip(self.values, other.values))

    def __mul__(self, scalar):
        factor = _finite_number(scalar, "scalar")
        return Vector(value * factor for value in self.values)

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("dot product requires another Vector")
        if len(self) != len(other):
            raise ValueError("vector dimensions must match")
        return sum(a * b for a, b in zip(self.values, other.values))

    def __matmul__(self, other):
        return self.dot(other)

    def norm(self):
        return math.hypot(*self.values)


@dataclass(frozen=True, init=False)
class Matrix:
    """A nonempty rectangular matrix of finite real elements."""

    rows: tuple

    def __init__(self, rows):
        raw_rows = _items(rows, "matrix")
        if not raw_rows:
            raise ValueError("matrix must have at least one row")
        validated = []
        width = None
        for raw_row in raw_rows:
            elements = _items(raw_row, "matrix row")
            if not elements:
                raise ValueError("matrix must have at least one column")
            if width is None:
                width = len(elements)
            elif len(elements) != width:
                raise ValueError("matrix rows must have equal lengths")
            validated.append(tuple(
                _finite_number(value, "matrix element") for value in elements
            ))
        object.__setattr__(self, "rows", tuple(validated))

    @property
    def shape(self):
        return (len(self.rows), len(self.rows[0]))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("matrix addition requires another Matrix")
        if self.shape != other.shape:
            raise ValueError("matrix shapes must match")
        return Matrix(
            (a + b for a, b in zip(left, right))
            for left, right in zip(self.rows, other.rows)
        )

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("matrix subtraction requires another Matrix")
        if self.shape != other.shape:
            raise ValueError("matrix shapes must match")
        return Matrix(
            (a - b for a, b in zip(left, right))
            for left, right in zip(self.rows, other.rows)
        )

    def __mul__(self, scalar):
        factor = _finite_number(scalar, "scalar")
        return Matrix((value * factor for value in row) for row in self.rows)

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        height, width = self.shape
        if isinstance(other, Vector):
            if width != len(other):
                raise ValueError("matrix columns must match vector dimension")
            return Vector(
                sum(a * b for a, b in zip(row, other.values))
                for row in self.rows
            )
        if isinstance(other, Matrix):
            other_height, _ = other.shape
            if width != other_height:
                raise ValueError("left columns must match right rows")
            columns = tuple(zip(*other.rows))
            return Matrix(
                (sum(a * b for a, b in zip(row, column)) for column in columns)
                for row in self.rows
            )
        raise TypeError("matrix multiplication requires Matrix or Vector")

    def transpose(self):
        return Matrix(zip(*self.rows))
