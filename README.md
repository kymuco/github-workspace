# GitHub Workspace

## Linear algebra

`linear_algebra.py` provides an immutable `Vector` and `Matrix` API using only the Python standard library. Vectors have at least one component; matrices have at least one row and one column and must be rectangular. Elements and scalars must be finite real numbers (booleans are not accepted). Invalid types raise `TypeError`; non-finite values, empty inputs and incompatible dimensions raise `ValueError`.

### Vectors

- `Vector([x1, x2, ...])` supports arbitrary positive dimension.
- `a + b`, `a - b`: component-wise arithmetic for matching dimensions.
- `a * scalar`, `scalar * a`: scalar multiplication.
- `a.dot(b)` or `a @ b`: dot product.
- `a.norm()`: Euclidean norm.
- Components are available as an immutable tuple in `a.values`.

### Matrices

- `Matrix([[a, b], [c, d]])` accepts nonempty rectangular rows; `m.shape` is `(rows, columns)`.
- `a + b`, `a - b`: element-wise arithmetic for equal shapes.
- `a * scalar`, `scalar * a`: scalar multiplication.
- `a @ b`: matrix multiplication; `a @ vector`: matrix–vector product.
- `a.transpose()`: transposed matrix; `a.rows` is an immutable tuple of tuples.

```python
from linear_algebra import Matrix, Vector

v = Vector([3, 4])
print(v.norm())                 # 5.0
print(v.dot(Vector([1, 2])))   # 11.0

m = Matrix([[1, 2], [3, 4]])
print((m @ v).values)           # (11.0, 25.0)
print(m.transpose().rows)      # ((1.0, 3.0), (2.0, 4.0))
```

All arithmetic returns new objects; original inputs are not modified. Determinants and matrix inversion are **not implemented** in this initial stage.

### Tests

From the repository root, run:

```sh
python -m unittest discover -v
```

The test suite in `test_linear_algebra.py` covers vector and matrix operations, rectangular dimensions, fractional and negative elements, immutability and validation errors.
