import unittest
from find_median_two import findMedianSortedArrays

TEST_CASES = [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3, 4, 5], [6], 3.5),
        ([], [1], 1),
        ([1, 4, 7],  [2, 3, 6], 3.5),
        ([1, 2, 3], [10, 11, 12],  6.5),
        ([1, 2, 2], [2, 2, 3], 2),
        ([1, 2, 3, 4, 100], [101, 102],  4)
    ]

class TestFindMedian(unittest.TestCase):
    def test_median_of_two_lists(self):
        for a, b, expected in TEST_CASES:
            result = findMedianSortedArrays(a, b)
            self.assertAlmostEqual(
                result,
                expected,
                msg=f"Failed for inputs {a} and {b}"
            )

if __name__ == "__main__":
    unittest.main()