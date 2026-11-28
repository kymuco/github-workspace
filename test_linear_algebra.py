"""Unittest coverage for the linear_algebra module."""

from dataclasses import FrozenInstanceError
import math
import unittest

from linear_algebra import Matrix, Vector


class ApproximateAssertions:
    def assertVectorAlmostEqual(self, vector, expected):
        self.assertIsInstance(vector, Vector)
        self.assertEqual(len(vector.values), len(expected))
        for actual, target in zip(vector.values, expected):
            self.assertAlmostEqual(actual, target)

    def assertMatrixAlmostEqual(self, matrix, expected):
        self.assertIsInstance(matrix, Matrix)
        self.assertEqual(matrix.shape, (len(expected), len(expected[0])))
        for actual_row, expected_row in zip(matrix.rows, expected):
            for actual, target in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, target)


class VectorTests(ApproximateAssertions, unittest.TestCase):
    def test_arbitrary_positive_dimensions(self):
        self.assertVectorAlmostEqual(Vector([1, -2.5, 0, 3, 4]), [1, -2.5, 0, 3, 4])
        self.assertEqual(len(Vector([7])), 1)

    def test_addition(self):
        a = Vector([1.5, -2, 0])
        b = Vector([-3, 0.25, 4])
        self.assertVectorAlmostEqual(a + b, [-1.5, -1.75, 4])
        self.assertVectorAlmostEqual(a, [1.5, -2, 0])

    def test_subtraction(self):
        self.assertVectorAlmostEqual(
            Vector([1.5, -2, 0]) - Vector([-3, 0.25, 4]),
            [4.5, -2.25, -4],
        )

    def test_scalar_multiplication(self):
        v = Vector([-2, 1.5])
        self.assertVectorAlmostEqual(v * -0.5, [1, -0.75])
        self.assertVectorAlmostEqual(2.5 * v, [-5, 3.75])
        self.assertVectorAlmostEqual(v * 0, [0, 0])

    def test_dot_and_matmul(self):
        a, b = Vector([1.5, -2, 3]), Vector([-4, 0.5, 2])
        self.assertAlmostEqual(a.dot(b), -1)
        self.assertAlmostEqual(a @ b, -1)

    def test_norm(self):
        self.assertAlmostEqual(Vector([-3, 4]).norm(), 5)
        self.assertAlmostEqual(Vector([0, 0, 0]).norm(), 0)
        self.assertAlmostEqual(Vector([0.5]).norm(), 0.5)

    def test_mismatched_dimensions(self):
        a, b = Vector([1, 2]), Vector([1, 2, 3])
        for operation in (lambda: a + b, lambda: a - b,
                          lambda: a.dot(b), lambda: a @ b):
            with self.subTest(operation=operation), self.assertRaises(ValueError):
                operation()

    def test_invalid_elements_and_dimensions(self):
        with self.assertRaises(ValueError):
            Vector([])
        for value in (math.inf, -math.inf, math.nan):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Vector([value])
        for value in (True, "2", None, 2 + 1j):
            with self.subTest(value=value), self.assertRaises(TypeError):
                Vector([value])
        with self.assertRaises(TypeError):
            Vector(5)

    def test_invalid_operand_types(self):
        v = Vector([1, 2])
        for operation in (lambda: v + [1, 2], lambda: v - 2,
                          lambda: v.dot([1, 2]), lambda: v @ 2,
                          lambda: v * "2", lambda: "2" * v):
            with self.subTest(operation=operation), self.assertRaises(TypeError):
                operation()
        for scalar in (math.inf, math.nan):
            with self.subTest(scalar=scalar), self.assertRaises(ValueError):
                v * scalar

    def test_immutability(self):
        v = Vector([1, 2])
        self.assertVectorAlmostEqual(v + Vector([3, 4]), [4, 6])
        self.assertVectorAlmostEqual(v, [1, 2])
        with self.assertRaises(FrozenInstanceError):
            v.values = (9, 9)
        with self.assertRaises(TypeError):
            v.values[0] = 9


class MatrixTests(ApproximateAssertions, unittest.TestCase):
    def test_rectangular_shape_and_fractional_values(self):
        matrix = Matrix([[1.5, -2, 3], [0, 4.25, -5]])
        self.assertEqual(matrix.shape, (2, 3))
        self.assertMatrixAlmostEqual(matrix, [[1.5, -2, 3], [0, 4.25, -5]])

    def test_single_element(self):
        matrix = Matrix([[2.5]])
        self.assertEqual(matrix.shape, (1, 1))
        self.assertMatrixAlmostEqual(matrix @ matrix, [[6.25]])

    def test_addition(self):
        a = Matrix([[1, -2], [3.5, 4]])
        b = Matrix([[0.5, 3], [-1, -2]])
        self.assertMatrixAlmostEqual(a + b, [[1.5, 1], [2.5, 2]])
        self.assertMatrixAlmostEqual(a, [[1, -2], [3.5, 4]])

    def test_subtraction(self):
        self.assertMatrixAlmostEqual(
            Matrix([[1, -2], [3.5, 4]]) - Matrix([[0.5, 3], [-1, -2]]),
            [[0.5, -5], [4.5, 6]],
        )

    def test_scalar_multiplication(self):
        matrix = Matrix([[1, -2], [0.5, 3]])
        self.assertMatrixAlmostEqual(matrix * -2, [[-2, 4], [-1, -6]])
        self.assertMatrixAlmostEqual(0.5 * matrix, [[0.5, -1], [0.25, 1.5]])
        self.assertMatrixAlmostEqual(matrix * 0, [[0, 0], [0, 0]])

    def test_rectangular_matrix_product(self):
        a = Matrix([[1, 2, 3], [4, -1, 0.5]])
        b = Matrix([[2, 0], [-1, 3], [0.5, 4]])
        self.assertMatrixAlmostEqual(a @ b, [[1.5, 18], [9.25, -1]])

    def test_matrix_vector_product(self):
        a = Matrix([[1.5, -2, 3], [4, 0, -1]])
        b = Vector([2, -1, 0.5])
        self.assertVectorAlmostEqual(a @ b, [6.5, 7.5])

    def test_transpose(self):
        a = Matrix([[1, 2, 3], [-4, 5, 6]])
        self.assertMatrixAlmostEqual(a.transpose(), [[1, -4], [2, 5], [3, 6]])
        self.assertMatrixAlmostEqual(a, [[1, 2, 3], [-4, 5, 6]])
        self.assertMatrixAlmostEqual(Matrix([[1, 2, 3]]).transpose(),
                                     [[1], [2], [3]])

    def test_invalid_shape(self):
        for rows in ([], [[]], [[1, 2], [3]], [[1], []]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                Matrix(rows)
        with self.assertRaises(TypeError):
            Matrix(5)
        with self.assertRaises(TypeError):
            Matrix([[1, 2], 3])

    def test_invalid_elements(self):
        for value in (math.inf, -math.inf, math.nan):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Matrix([[1, value]])
        for value in (True, "3", None, 1j):
            with self.subTest(value=value), self.assertRaises(TypeError):
                Matrix([[1, value]])

    def test_mismatched_shapes(self):
        a, b = Matrix([[1, 2]]), Matrix([[1], [2]])
        for operation in (lambda: a + b, lambda: a - b,
                          lambda: b @ b, lambda: a @ Vector([1])):
            with self.subTest(operation=operation), self.assertRaises(ValueError):
                operation()

    def test_invalid_operand_types(self):
        a = Matrix([[1, 2]])
        for operation in (lambda: a + [[1, 2]], lambda: a - 3,
                          lambda: a * [1, 2], lambda: a @ [1, 2],
                          lambda: a * True):
            with self.subTest(operation=operation), self.assertRaises(TypeError):
                operation()
        for scalar in (math.inf, math.nan):
            with self.subTest(scalar=scalar), self.assertRaises(ValueError):
                a * scalar

    def test_immutability(self):
        a = Matrix([[1, 2], [3, 4]])
        self.assertMatrixAlmostEqual(a * 2, [[2, 4], [6, 8]])
        self.assertMatrixAlmostEqual(a, [[1, 2], [3, 4]])
        with self.assertRaises(FrozenInstanceError):
            a.rows = ((9, 9),)
        with self.assertRaises(TypeError):
            a.rows[0][0] = 9


if __name__ == "__main__":
    unittest.main()
