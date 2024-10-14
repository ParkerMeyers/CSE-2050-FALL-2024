import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort, merge


class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""

    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0], matrix[1], matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """
        Test case for an empty list.
        """
        empty_array = [[], [], []]
        self.assertEqual(self.sorting_alg(empty_array), ([], 0))

    def test_sorted(self):
        """
        Test case for a sorted list.
        """
        sorted_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Unpack the sorted row and the number of swaps
        sorted_row, swaps = self.sorting_alg(sorted_matrix)
        # Check if the row is sorted
        self.assertTrue(self.is_sorted(sorted_row))



    def test_reverse_sorted(self):
        """
        Test case for a reverse sorted list.
        """
        reverse_sorted_matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        sorted_row, swaps = self.sorting_alg(reverse_sorted_matrix)
        self.assertTrue(self.is_sorted(sorted_row))

        self.assertEqual(swaps, 3)


    def test_random(self):
        """
        Test case for a random list.
        """
        reverse_sorted_matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        sorted_row, swaps = self.sorting_alg(reverse_sorted_matrix)
        self.assertTrue(self.is_sorted(sorted_row))



class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)



class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""

    def setUp(self):
        """Set up the insertion sort algorithm for testing."""
        super().setUp(insertion_sort)


class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""

    def setUp(self):
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)

    def test_reverse_sorted(self):
        """
        Test case for a reverse sorted list.
        """
        reverse_sorted_matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        sorted_row, swaps = self.sorting_alg(reverse_sorted_matrix)
        self.assertTrue(self.is_sorted(sorted_row))

        self.assertEqual(swaps, 1)

    def test_random(self):
        """
        Test case for a random list.
        """
        random_matrix = [[5, 2, 7], [3, 8, 1], [6, 4, 9]]
        sorted_row, swaps = self.sorting_alg(random_matrix)
        self.assertTrue(self.is_sorted(sorted_row))


if __name__ == "__main__":
    unittest.main()
