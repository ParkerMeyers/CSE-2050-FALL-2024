import unittest
from solve_puzzle import solve_puzzle

class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
        """Tests a board solvable using only CW moves"""
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 0]))
        self.assertTrue(solve_puzzle([1, 2, 3, 0, 4]))
        self.assertTrue(solve_puzzle([1, 2, 0, 3, 4]))
        self.assertTrue(solve_puzzle([3, 2, 1, 4, 2, 3, 1, 2, 4, 1]))

    def testCounterClockwise(self):
        """Tests a board solvable using only CCW moves"""
        self.assertTrue(solve_puzzle([2, 3, 1, 4, 2, 3, 1, 2, 4, 1]))
        self.assertTrue(solve_puzzle([4, 3, 1, 2, 4, 3, 1, 2, 4, 1]))
        self.assertTrue(solve_puzzle([1, 4, 3, 2, 1, 3, 2, 4, 1, 2]))
        self.assertTrue(solve_puzzle([3, 1, 4, 2, 3, 1, 2, 4, 1, 2]))

    def testMixed(self):
        """Tests a board solvable using a combination of CW and CCW moves"""
        self.assertTrue(solve_puzzle([1, 2, 3, 0, 4, 5, 6, 7, 8]))
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 0, 5, 6, 7, 8]))
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 5, 0, 6, 7, 8]))
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 5, 6, 0, 7, 8]))
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 5, 6, 7, 0, 8]))
        self.assertTrue(solve_puzzle([1, 2, 3, 4, 5, 6, 7, 8, 0]))

    def testUnsolveable(self):
        """Tests an unsolvable board"""
        self.assertFalse(solve_puzzle([3, 4, 1, 2, 0]))
        self.assertFalse(solve_puzzle([0, 1, 2, 3, 0]))
        self.assertFalse(solve_puzzle([9, 1, 9, 3, 9, 92]))

if __name__ == '__main__':
    unittest.main()