import unittest

from linkedlist import Node, LinkedList


class TestNode(unittest.TestCase):
    def test_attributes(self):
        # Test that the linked list has the correct attributes
        linked_list = Node(1)
        self.assertEqual(linked_list.item, 1)
        self.assertIsNone(linked_list.link)

    def test_repr(self):
        # Test that the __repr__ method returns the correct string
        linked_list = Node(1)
        self.assertEqual(str(linked_list), 'Node(1)')


class TestLinkedList(unittest.TestCase):
    def test_empty_linked_list(self):
        # Test that the linked list is empty when initialized
        linked_list = LinkedList()
        self.assertIsNone(linked_list.get_head())
        self.assertIsNone(linked_list.get_tail())
        self.assertEqual(linked_list._len, 0)

    def test_add_last(self):
        # Test that add_last adds an item to the end of the linked list
        linked_list = LinkedList()

        # Sequentially add items to end of LinkedList. Making sure that you get the correct values
        for i in range(1, 100, 2):
            linked_list.add_last(i)
            self.assertEqual(linked_list._len, i // 2 + 1)
            self.assertEqual(linked_list.get_head(), 1)
            self.assertEqual(linked_list.get_tail(), i)

    def test_non_empty_linked_list(self):
        # Test linked list with various iterable items
        linked_list_one = LinkedList(['a', 'b', 'c'])
        linked_list_two = LinkedList(range(10))

        # Check the first linked list
        self.assertEqual(linked_list_one.get_head(), 'a')
        self.assertEqual(linked_list_one.get_tail(), 'c')
        self.assertEqual(linked_list_one._len, 3)

        # Check the second linked list
        self.assertEqual(linked_list_two.get_head(), 0)
        self.assertEqual(linked_list_two.get_tail(), 9)
        self.assertEqual(linked_list_two._len, 10)

    def test_add_first(self):
        # Test that add_first adds an item to the beginning of the linked list
        linked_list = LinkedList()

        # Sequentially add items to beginning of LinkedList. Making sure that you get the correct values
        for i in range(1, 100, 2):
            linked_list.add_first(i)
            self.assertEqual(linked_list._len, i // 2 + 1)
            self.assertEqual(linked_list.get_head(), i)
            self.assertEqual(linked_list.get_tail(), 1)

    def test_remove_first(self):
        # Test that remove_first removes the first item from the linked list
        linked_list = LinkedList(range(10))

        # Sequentially remove items from the beginning of LinkedList. Making sure that you get the correct values
        for i in range(10):
            self.assertEqual(linked_list.remove_first(), i)
            self.assertEqual(linked_list._len, 9 - i)
            if len(linked_list) > 0:
                self.assertEqual(linked_list.get_head(), i + 1)
                self.assertEqual(linked_list.get_tail(), 9)

    def test_remove_last(self):
        # Test that remove_last removes the last item from the linked list
        linked_list = LinkedList(range(10))

        # Sequentially remove items from the end of LinkedList. Making sure that you get the correct values
        for i in range(9, -1, -1):
            self.assertEqual(linked_list.remove_last(), i)
            self.assertEqual(linked_list._len, i)
            if len(linked_list) > 0:
                self.assertEqual(linked_list.get_head(), 0)
                self.assertEqual(linked_list.get_tail(), i - 1)
