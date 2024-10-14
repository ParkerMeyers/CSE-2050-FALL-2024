import unittest

from process import Process


class TestProcess(unittest.TestCase):
    def test_init_only_name(self):
        # Make sure the attributes are set correctly
        process = Process("p1")
        self.assertEqual(process.pid, "p1")
        self.assertEqual(process.cycles, 100)
        self.assertIsNone(process.link)
        self.assertIsNone(process.prev)

    def test_init_name_and_cycles(self):
        # Make sure the attributes are set correctly
        process = Process("p1", 150)
        self.assertEqual(process.pid, "p1")
        self.assertEqual(process.cycles, 150)
        self.assertIsNone(process.link)
        self.assertIsNone(process.prev)

    def test_eq_only_name(self):
        # Test that the names are the same
        process1 = Process("p1")
        process2 = Process("p1")
        self.assertEqual(process1, process2)

    def test_eq_name_and_cycles(self):
        # Shouldn't matter that cycles are different, Test if the equality check only checks the name
        process1 = Process("p1", 150)
        process2 = Process("p1", 125)
        self.assertEqual(process1, process2)

    def test_eq_different_name(self):
        # Test that they are not equal
        process1 = Process("p1")
        process2 = Process("p2")
        self.assertNotEqual(process1, process2)

    def test_repr(self):
        # Test the string representation
        process = Process("p1", 150)
        self.assertEqual(repr(process), "Process(p1, 150)")
