import unittest
from loop_rotate import loop_rotate


class TestLoopRotate(unittest.TestCase):

    def test_basic_rotations(self):
        arr = [1, 2, 3, 4, 5]

        test_cases = [
            (1, [5, 1, 2, 3, 4]),
            (2, [4, 5, 1, 2, 3]),
            (3, [3, 4, 5, 1, 2]),
            (4, [2, 3, 4, 5, 1]),
            (5, [1, 2, 3, 4, 5]),  # full rotation
        ]

        for k, expected in test_cases:
            with self.subTest(k=k):
                self.assertEqual(loop_rotate(k, arr), expected)

    def test_rotation_larger_than_length(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(loop_rotate(6, arr), [5, 1, 2, 3, 4])

    def test_empty_array(self):
        self.assertEqual(loop_rotate(3, []), [])

    def test_zero_rotation(self):
        self.assertEqual(loop_rotate(0, [1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
