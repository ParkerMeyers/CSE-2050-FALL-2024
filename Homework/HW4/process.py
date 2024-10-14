class Process:
    def __init__(self, pid, cycles=100):
        """
        Constructor for the Process class
        :param pid: str: A unique process ID
        :param cycles: int (default=100): Number of clock cycles required to complete this process.
        """
        self.pid = pid
        self.cycles = cycles

        # Link to the next process in the circular queue
        self.link = None
        # Link to the previous process in the circular queue
        self.prev = None

    def __eq__(self, other):
        """
        Compares two processes, they are considered equal if they have the same pid
        :param other: Process: The process to compare self to
        :return: bool: True if the processes are equal, False otherwise
        """
        return self.pid == other.pid

    def __repr__(self):
        return f"Process({self.pid}, {self.cycles})"
