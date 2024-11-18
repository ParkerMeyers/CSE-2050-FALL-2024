def idx_left(L, idx, right):
    """
    Returns the index of the left child of `idx`, or None if that is not less than `right`.
    Return:
        int: The index of the left child of `idx`, or None if that is not less than `right`.
    """
    left = 2 * idx + 1
    if left >= right:
        return None
    return left


def idx_right(L, idx, right):
    """
    Returns the index of the right child of `idx`, or None if that is not less than `right`.
    Return:
        int: The index of the right child of `idx`, or None
    """
    right_idx = 2 * idx + 2
    if right_idx >= right:
        return None
    return right_idx


def idx_max_child(L, idx, right):
    """
    Returns the index of the max child of `idx`, or None if that is not less than `right`.
    Return:
        int: The index of the max child of `idx`, or None if that is not less than `right`.
    """
    left = idx_left(L, idx, right)
    right = idx_right(L, idx, right)
    if left is None:
        return None
    if right is None or L[left] > L[right]:
        return left
    return right


def swap(L, i, j):
    """
    Swaps the items at indices `i` and `j`.
    """
    L[i], L[j] = L[j], L[i]


def downheap(L, idx, right):
    """
    Repeatedly downheaps the item at index `idx` until the array is heap-ordered from `idx:right`, excluding the item at index `right`.
    """
    child = idx_max_child(L, idx, right)
    while child is not None and L[child] > L[idx]:
        swap(L, idx, child)
        idx = child
        child = idx_max_child(L, idx, right)


def heapsort(L):
    """
    Implements the heapsort algorithm.
    """
    n = len(L)
    # Create a max-heap in O(n)
    for i in range(n // 2 - 1, -1, -1):
        downheap(L, i, n)
    # Until L is a sorted array
    for i in range(n - 1, 0, -1):
        swap(L, 0, i)
        downheap(L, 0, i)
