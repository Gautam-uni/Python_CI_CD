import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 6), -1)

    def test_empty(self):
        self.assertEqual(binary_search([], 1), -1)

if __name__ == "__main__":
    unittest.main()
