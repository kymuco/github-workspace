# GitHub Workspace

## Geometry module

A minimal Python geometry library in `geometry.py` (standard library only).

- `Circle(radius)`: `area()` uses `math.pi * radius ** 2`; `perimeter()` returns the circumference.
- `Rectangle(width, height)`: `area()` and `perimeter()` for a rectangle.
- `Triangle(a, b, c)`: `area()` uses Heron's formula; `perimeter()` sums the three sides.

Dimensions must be positive, finite real numbers. Invalid dimensions, including zero, negative or non-finite values, raise `ValueError`. Triangle sides must also satisfy the **strict triangle inequalities**, otherwise `ValueError` is raised.

### Example

```python
from geometry import Circle, Rectangle, Triangle

print(Circle(2).area())           # 12.566370614359172
print(Rectangle(3, 4).perimeter()) # 14
print(Triangle(3, 4, 5).area())    # 6.0
```

### Tests

Run from the repository root:

```sh
python -m unittest discover -v
```

The tests are in `test_geometry.py` and use `assertAlmostEqual` for floating-point results.
