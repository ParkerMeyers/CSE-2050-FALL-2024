# This file empty on purpose - add the correct classes/methods below

class Entry:
    """
    Entry class to represent an entry in a priority queue
    """
    def __init__(self, item, priority):
        """
        Constructor for Entry class

        Arguments:
            item: the key for the entry
            priority: the priority for the entry
        """
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """
        Equality operator for Entry class

        Arguments:
            other: the other entry to compare to

        Returns:
            True if the items and priorities are equal, False otherwise
        """
        return self.item == other.item and self.priority == other.priority

    def __lt__(self, other):
        """
        Less than operator for Entry class

        Arguments:
            other: the other entry to compare to

        Returns:
            True if the priority of this entry is less than the other entry, False otherwise
        """
        return self.priority < other.priority

class PQ_UL:
    """
    Priority queue ADT with unordered list data structure
    """
    def __init__(self):
        """
        Constructor for PQ_UL class
        """
        self._data = []

    def __len__(self):
        """
        Length operator for PQ_UL class

        Returns:
            The number of elements in the priority queue
        """
        return len(self._data)

    def insert(self, item, priority):
        """
        Inserts a new entry into the priority queue

        Arguments:
            item: the key for the entry
            priority: the priority for the entry
        """
        self._data.append(Entry(item, priority))

    def find_min(self):
        """
        Finds the entry with the minimum priority in the priority queue

        Returns:
            The entry with the minimum priority
        """
        if len(self._data) == 0:
            return None

        min_entry = self._data[0]
        for entry in self._data:
            if entry < min_entry:
                min_entry = entry

        return min_entry

    def remove_min(self):
        """
        Removes the entry with the minimum priority from the priority queue

        Returns:
            The entry with the minimum priority
        """
        if len(self._data) == 0:
            return None

        min_entry = self.find_min()
        self._data.remove(min_entry)
        return min_entry

class PQ_OL:
    """
    Priority queue ADT with ordered (sorted) list data structure
    """
    def __init__(self):
        """
        Constructor for PQ_OList class
        """
        self._data = []

    def __len__(self):
        """
        Length operator for PQ_OList class

        Returns:
            The number of elements in the priority queue
        """
        return len(self._data)

    def insert(self, item, priority):
        """
        Inserts a new entry into the priority queue

        Arguments:
            item: the key for the entry
            priority: the priority for the entry
        """
        new_entry = Entry(item, priority)
        self._data.append(new_entry)
        self._data.sort()

    def find_min(self):
        """
        Finds the entry with the minimum priority in the priority queue

        Returns:
            The entry with the minimum priority
        """
        if len(self._data) == 0:
            return None

        return self._data[0]

    def remove_min(self):
        """
        Removes the entry with the minimum priority from the priority queue

        Returns:
            The entry with the minimum priority
        """
        if len(self._data) == 0:
            return None

        return self._data.pop(0)