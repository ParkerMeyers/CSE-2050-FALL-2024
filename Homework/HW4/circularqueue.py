class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""

    def __init__(self, processes=None):
        """
        Constructor for the CircularQueue class
        :param processes: list (default=None): A list of Process objects to initialize the queue with
        """
        self._head = None
        self._len = 0
        self._d_processes = {}

        if processes:
            for process in processes:
                self.add_process(process)

    def __len__(self):
        """
        :return: int: The number of processes in the queue
        """
        return self._len

    def __repr__(self):
        """
        :return: str: A string representation of the queue
        """
        if self._len == 0:
            return "CircularQueue()"

        processes = []
        current = self._head

        for _ in range(self._len):
            processes.append(repr(current))
            current = current.link

        return f"CircularQueue({', '.join(processes)})"

    def add_process(self, process):
        """
        Adds process to end of queue (just before self._head).
        If a process is the only process in a circular queue (i.e. len(self) == 1), it's link and prev attributes should point to itself
        :param process: Process: The process to add to the queue
        """
        if self._len == 0:
            self._head = process
            process.link = process
            process.prev = process
        else:
            tail = self._head.prev
            tail.link = process
            process.prev = tail
            process.link = self._head
            self._head.prev = process
        self._d_processes[process.pid] = process
        self._len += 1

    def remove_process(self, process):
        """
        Removes and returns a specified Process from the queue. N
        ote that the input here is the actual Process object which should be removed, not its pid.
        :param process: Process: The process to remove from the queue
        :return: Process: The process that was removed
        """
        if self._len == 0:
            raise ValueError("Queue is empty")
        if self._len == 1:
            self._head = None
        else:
            process.prev.link = process.link
            process.link.prev = process.prev
            if process == self._head:
                self._head = process.link
        self._d_processes.pop(process.pid)
        self._len -= 1
        return process

    def kill(self, pid):
        """
         removes and returns a process with the given pid. add a dictionary self._d_processes to the queue that maps pids to Process objects. This dictionary will need to be updated whenever you add or remove a process (e.g. self._d_processes[pid] = node or self._d_processes.pop(pid)).
        """
        if pid not in self._d_processes:
            raise ValueError(f"No process with pid {pid}")
        process = self._d_processes[pid]
        return self.remove_process(process)

    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []  # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(
                    f"{self._head.pid} finished after {n_cycles - n_remaining + 1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link

            n_remaining -= 1

        return '\n'.join(return_strings)
