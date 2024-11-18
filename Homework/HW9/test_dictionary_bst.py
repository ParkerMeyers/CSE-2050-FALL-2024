import unittest

from dictionary_bst import DictionaryBST


class TestDictionaryBST(unittest.TestCase):
    """
    A class to test the DictionaryBST class.

    Methods:
        setUp(): Create a new DictionaryBST object before each test.
        test_insert_and_search(): Test the insert and search methods.
        test_update_meaning(): Test updating the meaning of a word.
        test_print_alphabetical(): Test printing all dictionary entries in alphabetical order.
    """

    def setUp(self):
        """
        Create a new DictionaryBST object before each test.
        """
        self.dictionary = DictionaryBST()

    def test_insert_and_search(self):
        """
        Test the insert and search methods.
        """
        self.dictionary.insert("whale shark", "The largest fish in the sea.")
        self.dictionary.insert("manta ray", "A large, flat fish with wing-like pectoral fins.")
        self.dictionary.insert("clownfish", "A small, colorful fish often found in coral reefs.")

        self.assertEqual(self.dictionary.search("whale shark"), "The largest fish in the sea.")
        self.assertEqual(self.dictionary.search("manta ray"), "A large, flat fish with wing-like pectoral fins.")
        self.assertEqual(self.dictionary.search("clownfish"), "A small, colorful fish often found in coral reefs.")
        self.assertIsNone(self.dictionary.search("great white shark"))

    def test_update_meaning(self):
        """
        Test updating the meaning of a word.
        """
        self.dictionary.insert("whale shark", "The largest fish in the sea.")
        self.dictionary.insert("whale shark", "A gentle giant of the ocean.")

        self.assertEqual(self.dictionary.search("whale shark"), "A gentle giant of the ocean.")

    def test_print_alphabetical(self):
        """
        Test printing all dictionary entries in alphabetical order.
        """
        self.dictionary.insert("whale shark", "The largest fish in the sea.")
        self.dictionary.insert("manta ray", "A large, flat fish with wing-like pectoral fins.")
        self.dictionary.insert("clownfish", "A small, colorful fish often found in coral reefs.")

        expected_output = [
            ("clownfish", "A small, colorful fish often found in coral reefs."),
            ("manta ray", "A large, flat fish with wing-like pectoral fins."),
            ("whale shark", "The largest fish in the sea.")
        ]
        self.assertEqual(self.dictionary.print_alphabetical(), expected_output)


if __name__ == '__main__':
    # Run the tests
    unittest.main()
