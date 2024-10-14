import unittest

from trib import trib


class TestTrib(unittest.TestCase):
    """
    Test the tribonacci function
    """

    def test_first_ten(self):
        """Tests the first ten numbers in the tribonacci sequence"""
        solutions = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 4, 7: 7, 8: 13, 9: 24, 10: 44}

        for k, v in solutions.items():
            # K is the key, V is the value
            self.assertEqual(trib(k), v)

    def test_large(self):
        """Test the 100th item in the tribonacci sequence (test a large number)"""
        self.assertEqual(trib(100), 28992087708416717612934417)
