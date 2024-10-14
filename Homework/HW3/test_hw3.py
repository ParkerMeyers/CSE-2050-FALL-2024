import unittest

import hw3


class TestCreateLists(unittest.TestCase):
    def test_normal_size(self):
        """
        Test that generate_lists returns two lists of the correct size
        """
        list1, list2 = hw3.generate_lists(10)
        self.assertEqual(len(list1), 10)
        self.assertEqual(len(list2), 10)

    def test_size_zero(self):
        """
        Test that generate_lists returns two empty lists when size is 0
        """
        list1, list2 = hw3.generate_lists(0)
        self.assertEqual(len(list1), 0)
        self.assertEqual(len(list2), 0)

    def test_large_size(self):
        """
        Test that generate_lists returns two lists of the correct size when size is large
        """
        list1, list2 = hw3.generate_lists(100000)
        self.assertEqual(len(list1), 100000)
        self.assertEqual(len(list2), 100000)

    def test_unique_elements(self):
        """
        Test that generate_lists returns two lists with unique elements
        """
        list1, list2 = hw3.generate_lists(10)
        self.assertEqual(len(set(list1)), len(list1))
        self.assertEqual(len(set(list2)), len(list2))

class TestFindCommon(unittest.TestCase):
    def test_normal_case(self):
        """
        Test that find_common returns the correct length of common elements
        """
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 2)

    def test_no_common_elements(self):
        """
        Test that find_common returns zero when there are no common elements
        """
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 0)

    def test_identical_lists(self):
        """
        Test that find_common returns the right count when the lists are identical
        """
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 3)

    def test_one_empty_list(self):
        """
        Test that find_common returns 0 when one of the lists is empty
        """
        list1 = [1, 2, 3]
        list2 = []
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 0)

    def test_both_empty_lists(self):
        """
        Test that find_common returns zero when both lists are empty
        """
        list1 = []
        list2 = []
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 0)

    def test_duplicate_elements(self):
        """
        Test that find_common returns the correct number of common elements when there are duplicates
        (even though the current implementation assumes unique elements)
        """
        list1 = [1, 2, 3, 3]
        list2 = [3, 3, 4, 5]
        common = hw3.find_common(list1, list2)
        self.assertEqual(common, 2)

class TestFindCommonEfficient(unittest.TestCase):
    def test_normal_case(self):
        """
        Test that find_common_efficient returns the correct number of common elements
        """
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 2)

    def test_no_common_elements(self):
        """
        Test that find_common_efficient returns 0 when there are no common elements
        """
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 0)

    def test_identical_lists(self):
        """
        Test that find_common_efficient returns the correct length when the lists are identical
        """
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 3)

    def test_one_empty_list(self):
        """
        Test that find_common_efficient returns 0 when one of the lists is empty
        """
        list1 = [1, 2, 3]
        list2 = []
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 0)

    def test_both_empty_lists(self):
        """
        Test that find_common_efficient returns 0 when both lists are empty
        """
        list1 = []
        list2 = []
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 0)

    def test_duplicate_elements(self):
        """
        Test that find_common_efficient returns the correct length of common elements when there are duplicates
        (even though the current implementation assumes unique elements)
        """
        list1 = [1, 2, 3, 3]
        list2 = [3, 3, 4, 5]
        common = hw3.find_common_efficient(list1, list2)
        self.assertEqual(common, 1)