import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes


class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L):
    """
    Scans a list from left to right and counts how many times an element is greater than the next element.
    Out of order pairs are referred to as inversions.
    Parameters:
        L (list): A list of integers
    Returns:
        MagicCase: The MagicCase that best describes the list to be used for sorting.
    """

    # Special Cases:
    # 1. If the list is sorted, return MagicCase.SORTED (n_inversions = 0)
    # 2. If fewer than some constant number of inversions, return MagicCase.CONSTANT_INVERSIONS (n_inversions < INVERSION_BOUND)
    # 3. If the list is reverse-sorted, return MagicCase.REVERSE_SORTED (n_inversions = len(L) - 1)
    # 4. Otherwise, return MagicCase.GENERAL (n_inversions = other)

    # Count the number of inversions in the list
    n_inversions = 0

    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            n_inversions += 1

    # Determine the MagicCase and return it
    if n_inversions == 0:
        return MagicCase.SORTED
    elif n_inversions == len(L) - 1:
        return MagicCase.REVERSE_SORTED
    elif n_inversions <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    else:
        return MagicCase.GENERAL


def reverse_list(L, alg_set=None):
    """
    Reverses a list in place

    Time Complexity: O(n)
    Space Complexity: O(1)
    Parameters:
        L (list): A list of integers
        alg_set (set): A set of names of the sorting algorithms used
    Returns:
        set: A set of names of the sorting algorithms used
    """
    # Keep track of the sorting algorithm used
    if alg_set is None:
        alg_set = set()
    alg_set.add("reverse_list")

    # Reverse the list, loop through the first half of the list and swap with the second half using an in place swap
    for i in range(len(L) // 2):
        # Swap the elements at the two indices at the same distance from the ends of the list
        L[i], L[-i - 1] = L[-i - 1], L[i]

    return alg_set


def magic_insertionsort(L, left, right, alg_set=None):
    """
    Sorts a sublist of integers using insertion sort. (from left to right)

    Time Complexity: O(n) for best case, O(n^2) for average and worst cases
    Space Complexity: O(1)
    Parameters:
        L (list): A list of integers
        left (int): The left index of the sublist to sort
        right (int): The right index of the sublist to sort
        alg_set (set): A set of names of the sorting algorithms used
    Returns:
        set: A set of names of the sorting algorithms used
    """
    # Keep track of the sorting algorithm used
    if alg_set is None:
        alg_set = set()
    alg_set.add("magic_insertionsort")

    # Loop through the list from the left index to the right index
    for i in range(left + 1, right):
        # Store the current element in a temporary variable
        current = L[i]
        # Store the index of the element to the left of the current element
        j = i - 1

        # Loop through the list from the current index to the left index using a while loop
        while j >= left and current < L[j]:
            # Shift the element to the right
            L[j + 1] = L[j]
            # Decrement the index
            j -= 1

        # Insert the current element in the correct position
        L[j + 1] = current

    return alg_set


def magic_mergesort(L, left, right, alg_set=None):
    """
    Sorts a sublist of integers using mergesort. (from left to right)

    Time Complexity: O(n log n) worst case
    Space Complexity: O(n)
    Parameters:
        L (list): A list of integers
        left (int): The left index of the sublist to sort
        right (int): The right index of the sublist to sort
        alg_set (set): A set of names of the sorting algorithms used
    Returns:
        set: A set of names of the sorting algorithms used
    """
    # Keep track of the sorting algorithm used
    if alg_set is None:
        alg_set = set()
    alg_set.add("magic_mergesort")

    # Call magic_insertionsort to sort sublists with 20 items or fewer. Quadratic sorting algorithms outperform nlogn algorithms on these small lists.
    if right - left <= 20:
        return magic_insertionsort(L, left, right, alg_set)

    # Calculate the middle index
    mid = (left + right) // 2

    # Recursively sort the left and right halves of the list
    magic_mergesort(L, left, mid, alg_set)
    magic_mergesort(L, mid, right, alg_set)

    # Merge the two sorted halves
    left_half = L[left:mid]
    right_half = L[mid:right]
    i = j = k = 0

    # Loop through the left and right halves and merge them
    while i < len(left_half) and j < len(right_half):
        # Compare the elements at the current indices and insert the smaller element into the list
        if left_half[i] < right_half[j]:
            L[left + k] = left_half[i]
            i += 1
        else:
            L[left + k] = right_half[j]
            j += 1
        k += 1

    # Insert any remaining elements from the left half into the list
    while i < len(left_half):
        L[left + k] = left_half[i]
        i += 1
        k += 1

    # Insert any remaining elements from the right half into the list
    while j < len(right_half):
        L[left + k] = right_half[j]
        j += 1
        k += 1

    return alg_set


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """
    Sorts a sublist of integers using quicksort. (from index left up to but not including the item at index right)

    Time Complexity: O(n log n) average case and worst case (uses magic_merge_sort when pivots are bad)
    Space Complexity: O(log n) for the recursive call stack, becomes O(n) in the worst case we have to sort using merge sort
    Parameters:
        L (list): A list of integers
        left (int): The left index of the sublist to sort
        right (int): The right index of the sublist to sort
        depth (int): The depth of the recursion
        alg_set (set): A set of names of the sorting algorithms used
    Returns:
        set: A set of names of the sorting algorithms used
    """
    # Keep track of the sorting algorithm used
    if alg_set is None:
        alg_set = set()
    alg_set.add("magic_quicksort")

    # Call magic_insertionsort to sort sublists with 20 items or fewer. Quadratic sorting algorithms outperform nlogn algorithms on these small lists.
    if right - left <= 20:
        return magic_insertionsort(L, left, right, alg_set)

    # If the depth of the recursion is greater than 3 * log2(n) + 1, use magic_mergesort to sort the list
    if depth > 3 * (math.log2(len(L)) + 1):
        return magic_mergesort(L, left, right, alg_set)

    # Choose the pivot as the last element in the sublist
    pivot = L[right - 1]
    i = left - 1

    # Loop through the sublist from the left index to the right index
    for j in range(left, right - 1):
        # If the current element is less than the pivot, increment the index i and swap the elements at indices i and j
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]

    # Swap the pivot with the element at index i + 1
    L[i + 1], L[right - 1] = L[right - 1], L[i + 1]

    # Recursively sort the left and right halves of the list
    magic_quicksort(L, left, i + 1, depth + 1, alg_set)
    magic_quicksort(L, i + 2, right, depth + 1, alg_set)

    return alg_set


def magicsort(L):
    """
    Sorts a list of integers using a combination of insertionsort, mergesort, and quicksort.

    Parameters:
        L (list): A list of integers
    Returns:
        set: A set of names of the sorting algorithms used
    """
    # Determine the MagicCase of the list
    case = linear_scan(L)

    # Create a set to store the names of the sorting algorithms used
    alg_set = set()

    # Sort the list based on the MagicCase
    if case == MagicCase.SORTED:
        # Already sorted
        pass
    elif case == MagicCase.REVERSE_SORTED:
        alg_set = reverse_list(L, alg_set)
    elif case == MagicCase.CONSTANT_INVERSIONS:
        alg_set = magic_insertionsort(L, 0, len(L), alg_set)
    else:
        alg_set = magic_quicksort(L, 0, len(L), 0, alg_set)

    return alg_set
