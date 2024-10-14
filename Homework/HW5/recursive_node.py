###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Recursively implements Linked List functionality"""

    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"

    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""
        # Base case: this sublist has a length of 1
        if self.link is None:
            return 1

        # Recursive case: this sublist has a length of 1 + the length of its link
        return 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
        # Base case: this is the tail node
        if self.link is None:
            return self.data

        # Recursive case: keep looking for the tail
        return self.link.get_tail()

    def add_last(self, data):
        """Recursively adds to end of this sublist"""
        # Base case: this is the last node
        if self.link is None:
            self.link = Node(data)
            return

        # Recursive case: keep looking for the last node
        self.link.add_last(data)

    def total(self):
        """Recursively adds all items"""
        # Base case: this is the last node
        if self.link is None:
            return self.data

        # Recursive case: keep adding
        return self.data + self.link.total()

    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
        # Base case: this is the last node
        if self.link is None:
            return None, self.data

        # Recursive case: keep looking for the last node
        new_head, tail_data = self.link.remove_last()
        self.link = new_head

        return self, tail_data

    def reverse(self, prev):
        """Recursively reverse list"""
        # Base case: this is the last node
        if self.link is None:
            self.link = prev
            return self

        # Recursive case: keep reversing
        new_head = self.link.reverse(self)
        self.link = prev

        return new_head
