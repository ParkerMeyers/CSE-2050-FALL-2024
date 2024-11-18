class Entry:
    def __init__(self, item, priority):
        """
        Initializes an Entry object with the given item and priority.
        Parameters:
            item: The item to be stored in the Entry object.
            priority: The priority of the item.
        """
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """
        Compares two Entry objects for equality based on their priority.
        Parameters:
            other: The other Entry object to compare with.
        Returns:
            True if the two Entry objects have the same priority, False otherwise.
        """
        return self.priority == other.priority

    def __lt__(self, other):
        """
        Compares two Entry objects based on their priority with the less than operator.
        Parameters:
            other: The other Entry object to compare with.
        Returns:
            True if the priority of the current Entry object is less than the priority of the other Entry object, False otherwise.
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        Compares two Entry objects based on their priority with the less than or equal to operator.
        Parameters:
            other: The other Entry object to compare with.
        Returns:
            True if the priority of the current Entry object is less than or equal to the priority of the other Entry object, False otherwise.
        """
        return self.priority <= other.priority

    def __repr__(self):
        """
        Returns a string representation of the Entry object.
        Returns:
            A string representation of the Entry object in the format "Entry(item=item, priority=priority)".
        """
        return f"Entry(item={self.item}, priority={self.priority})"
