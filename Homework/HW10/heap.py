from entry import Entry


class Heap:
    def __init__(self):
        """
        Initializes an empty heap.
        """
        self._L = []
        self._idx = {}

    def __len__(self):
        """
        Returns the number of items in the heap.
        """
        return len(self._L)

    def __iter__(self):
        """
        Yields the minimum entry until the heap is empty.
        """
        while len(self) > 0:
            yield self.remove_min()

    def idx_parent(self, idx):
        """
        Returns the index of the parent of the item at the given index.
        """
        if idx == 0:
            return None
        return (idx - 1) // 2

    def idx_left(self, idx):
        """
        Returns the index of the left child of the item at the given index.
        """
        left = 2 * idx + 1
        if left >= len(self):
            return None
        return left

    def idx_right(self, idx):
        """
        Returns the index of the right child of the item at the given index.
        """
        right = 2 * idx + 2
        if right >= len(self):
            return None
        return right

    def idx_min_child(self, idx):
        """
        Returns the index of the child with the smallest priority.
        """
        left = self.idx_left(idx)
        right = self.idx_right(idx)
        if left is None:
            return None
        if right is None or self._L[left] < self._L[right]:
            return left
        return right

    def insert(self, item, priority):
        """
        Inserts an item with the given priority into the heap.
        """
        entry = Entry(item, priority)
        self._L.append(entry)
        self._idx[item] = len(self) - 1
        self._upheap(len(self) - 1)

    def remove_min(self):
        """
        Removes and returns the item with the smallest priority from the heap.
        """
        if len(self) == 0:
            raise IndexError("remove_min from empty heap")
        self._swap(0, len(self) - 1)
        min_entry = self._L.pop()
        del self._idx[min_entry.item]
        if len(self) > 0:
            self._downheap(0)
        return min_entry

    def change_priority(self, item, priority):
        """
        Changes the priority of the item in the heap.
        """
        idx = self._idx[item]
        old_priority = self._L[idx].priority
        self._L[idx].priority = priority
        if priority < old_priority:
            self._upheap(idx)
        elif priority > old_priority:
            self._downheap(idx)
        return self._idx[item]

    def _swap(self, i, j):
        """
        Swaps the items at the given indices.
        """
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """
        Moves the item at the given index up the heap to restore the heap property.
        """
        parent = self.idx_parent(idx)
        while parent is not None and self._L[idx] < self._L[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = self.idx_parent(idx)

    def _downheap(self, idx):
        """
        Moves the item at the given index down the heap to restore the heap property.
        """
        child = self.idx_min_child(idx)
        while child is not None and self._L[child] < self._L[idx]:
            self._swap(idx, child)
            idx = child
            child = self.idx_min_child(idx)

    @staticmethod
    def heapify(entries):
        """
        Constructs a heap from the given list of entries.
        """
        heap = Heap()
        heap._L = entries
        heap._idx = {entry.item: i for i, entry in enumerate(entries)}
        for i in range(len(heap) - 1, -1, -1):
            heap._downheap(i)
        return heap
