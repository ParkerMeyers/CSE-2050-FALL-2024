# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

# Accessing and updating information should be O(1) time complexity and O(n) space complexity.


class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision=0):
        """
        Initializes a LocalRecord object with a position, max temperature, and min temperature.

        Parameters:
            pos (tuple): A tuple of two floats representing the position of the LocalRecord.
            max (float): The maximum temperature at the position.
            min (float): The minimum temperature at the position.
            precision (int): The number of decimal places to round the position to.
        """
        self.pos = (round(pos[0], precision), round(pos[1], precision))
        self.max = max
        self.min = min

    def add_report(self, temp):
        """
        Adds a temperature report to the LocalRecord object.

        Parameters:
            temp (float): The temperature to add to the Local
        """
        if self.max is None or temp > self.max:
            self.max = temp
        if self.min is None or temp < self.min:
            self.min = temp

    def __eq__(self, other):
        """
        Checks if two LocalRecord objects are equal.

        Parameters:
            other (LocalRecord): The LocalRecord object to compare to.
        """
        return self.pos == other.pos

    def __hash__(self):
        """
        Returns the hash value of the LocalRecord object.
        """
        return hash(self.pos)

    def __repr__(self):
        """
        Returns a string representation of the LocalRecord object.
        """
        return f"Record(pos={self.pos}, max={self.max}, min={self.min})"


class RecordsMap:
    def __init__(self):
        """
        Initializes a RecordsMap object with an empty dictionary of LocalRecord objects.
        """
        self._records = {}
        self._len = 0

    def __len__(self):
        """
        Returns the number of LocalRecord objects in the RecordsMap object.
        """
        return self._len

    def add_report(self, pos, temp):
        """
        Adds a temperature report to the RecordsMap object.

        Parameters:
            pos (tuple): A tuple of two floats representing the position of the LocalRecord.
            temp (float): The temperature to add to the Local
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        if rounded_pos not in self._records:
            self._records[rounded_pos] = LocalRecord(rounded_pos)
            self._len += 1
        self._records[rounded_pos].add_report(temp)

    def __getitem__(self, pos):
        """
        Returns the maximum and minimum temperatures for a given position.

        Parameters:
            pos (tuple): A tuple of two floats representing the position of the LocalRecord.

        Returns:
            tuple: A tuple of two floats representing the maximum and minimum temperatures at the position.
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        if rounded_pos not in self._records:
            raise KeyError(f"No records for pos {rounded_pos}.")
        record = self._records[rounded_pos]
        return record.min, record.max

    def __contains__(self, pos):
        """
        Checks if a given position is in the RecordsMap object.

        Parameters:
            pos (tuple): A tuple of two floats representing the position of the LocalRecord.

        Returns:
            bool: True if the position is in the RecordsMap object, False otherwise
        """
        rounded_pos = (round(pos[0], 0), round(pos[1], 0))
        return rounded_pos in self._records

    def _rehash(self, m_new):
        """
        Rehashes the LocalRecord objects in the RecordsMap object.

        Parameters:
            m_new (int): The new number of buckets to use.
        """
        new_records = {}
        for record in self._records.values():
            new_pos = (round(record.pos[0], 0), round(record.pos[1], 0))
            if new_pos not in new_records:
                new_records[new_pos] = LocalRecord(new_pos)
            new_records[new_pos].add_report(record.max)
            new_records[new_pos].add_report(record.min)
        self._records = new_records
