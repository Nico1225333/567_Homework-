"""Classify triangles and test the results."""

import unittest
from io import StringIO
from unittest.mock import patch


def classify_triangle(a, b, c):
    """Return the triangle type for three side lengths."""
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    if a == b == c:
        return 'Equilateral'

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right'

    if a == b or a == c or b == c:
        return 'Isoceles'

    return 'Scalene'


def run_classify_triangle(a, b, c):
    """Print the triangle classification."""
    print(f'classifyTriangle({a},{b},{c})={classify_triangle(a, b, c)}')


class TestTriangles(unittest.TestCase):
    """Test triangle classifications and printed output."""

    def test_set_1(self):
        """Check right triangles and invalid triangles."""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')

    def test_set_2(self):
        """Check equilateral, isosceles, and scalene triangles."""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classify_triangle(5, 5, 8), 'Isoceles')
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene')

    def test_print_output(self):
        """Check the text printed by the helper function."""
        with patch('sys.stdout', new_callable=StringIO) as output:
            run_classify_triangle(3, 4, 5)
            self.assertEqual(
                output.getvalue(),
                'classifyTriangle(3,4,5)=Right\n'
            )


if __name__ == '__main__':
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    unittest.main(exit=False)
