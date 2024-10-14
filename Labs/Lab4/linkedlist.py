class Node:
    def __init__(self, item, link=None):
        """
        Creates a new Node object
        :argument item: data to be stored in the node
        :argument link (default -> None): the next node in the linked list
        """
        self.item = item
        self.link = link

    def __repr__(self):
        """
        :return: a string representation of the node
        """
        return f'Node({self.item})'


class LinkedList:
    def __init__(self, items=None):
        """
        Creates a new LinkedList object
        :argument items (default -> None): an iterable of items to add to the linked list
        """
        self._head = None
        self._tail = None
        self._len = 0

        # Add the items to the linked list sequentially
        if items:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """
        :return: the number of items in the linked list
        """
        return self._len

    def get_head(self):
        """
        :return: the head of the linked list or None if the linked list is empty
        """
        return None if self._head is None else self._head.item

    def get_tail(self):
        """
        :return: the tail of the linked list or None if the linked list is empty
        """
        return None if self._tail is None else self._tail.item

    def add_first(self, item):
        """
        Adds an item to the beginning of the linked list
        :argument item: the data to be stored in the node
        """
        new_node = Node(item, self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._len += 1

    def add_last(self, item):
        """
        Adds an item to the end of the linked list
        :argument item: the data to be stored in the node
        """
        new_node = Node(item)
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.link = new_node
        self._tail = new_node
        self._len += 1

    def remove_first(self):
        """
        Removes the first node from the linked list
        :returns: the item from the first node in the linked list
        """
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty linked list')
        old_head = self._head
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._len -= 1
        return old_head.item

    def remove_last(self):
        """
        Removes the last node from the linked list
        :returns: the item from the last node in the linked list
        """
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty linked list')
        if self._head == self._tail:
            old_last = self._head
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.link != self._tail:
                current = current.link
            old_last = self._tail
            current.link = None
            self._tail = current
        self._len -= 1
        return old_last.item
