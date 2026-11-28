# GitHub Workspace

## Vector2 — two-dimensional vectors

`vector2.py` provides an immutable `Vector2(x, y)` class using only the Python standard library. Coordinates must be finite real numbers; invalid types raise `TypeError` and non-finite values raise `ValueError`.

| Operation | Example | Result |
| --- | --- | --- |
| Addition | `a + b` | New `Vector2` |
| Subtraction | `a - b` | New `Vector2` |
| Scalar multiplication | `a * 2`, `2 * a` | New `Vector2` |
| Scalar division | `a / 2` | New `Vector2` |
| Dot product | `a.dot(b)` | Number |
| Length | `a.length()` | Number |
| Distance | `a.distance_to(b)` | Number |
| Normalization | `a.normalized()` | New unit `Vector2` |

```python
from vector2 import Vector2

a = Vector2(3, 4)
b = Vector2(-1, 2)

print(a + b)             # Vector2(x=2.0, y=6.0)
print(a.dot(b))          # 5.0
print(a.length())        # 5.0
print(a.distance_to(b)) # sqrt(20)
print(a.normalized())    # Vector2(x=0.6, y=0.8)
```

Division by zero raises `ZeroDivisionError`. Normalizing the zero vector raises `ValueError`. Arithmetic never changes the input vectors. Invalid vector operands raise `TypeError`.

### Tests

Run from the repository root:

```sh
python -m unittest discover -v
```

Tests in `test_vector2.py` cover the operations, fractional and negative coordinates, error cases, and immutability.
