"""
tests for sort list module
"""
import unittest
from src.sort_list import sort_list


class TestSortList(unittest.TestCase):
    """test suite for sort list"""

    def test_sort_list(self):
        """
        Test if sortList can sort a list of integers
        """
        data = [2, 6, 4]
        result = sort_list(data)
        self.assertEqual(result, [2, 4, 6])

    def test_return_same(self):
        """
        If length = 1 return the same item.
        """
        data = [9]
        result = sort_list(data)
        self.assertEqual(result, data)

    def test_sort_immutable(self):
        """
        Test that the original list remains unmodified
        """
        data = [23, 6, 9, 4]
        result = sort_list(data)
        self.assertEqual(result, [4, 6, 9, 23])
        self.assertEqual(data, [23, 6, 9, 4])

    def test_negative(self):
        """
        test function can handle negative numbers correctly
        """
        data = [-23, 6, -9, 40000]
        result = sort_list(data)
        self.assertEqual(result, [-23, -9, 6, 40000])


if __name__ == "__main__":
    unittest.main()
