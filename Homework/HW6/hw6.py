def bubble_sort(matrix):
    """
    Sorts the first row of the matrix using the bubble sort algorithm.
    Parameters:
        matrix: The unsorted matrix
    Returns:
        A tuple containing the sorted first row list and the number of swaps performed

    """
    # Get the first row of the matrix if it exists
    if matrix[0]:
        first_row = matrix[0]
        n = len(first_row)
        swaps = 0
    else:
        return [], 0

    # Perform the bubble sort algorithm
    # Accesses each array element
    for i in range(n):
        # Compares each element with the next element
        for j in range(0, n - i - 1):
            # Compare the adjacent elements
            if first_row[j] > first_row[j + 1]:
                # Swap the elements if they are in the wrong order
                first_row[j], first_row[j + 1] = first_row[j + 1], first_row[j]
                swaps += 1

    return first_row, swaps

def insertion_sort(matrix):
    """
    Sorts the second row of the matrix using the insertion sort algorithm.
    Parameters:
        matrix: The unsorted matrix
    Returns:
        A tuple containing the sorted second row list and the number of swaps performed
    """
    # Get the second row of the matrix if it exists
    if matrix[1]:
        second_row = matrix[1]
        n = len(second_row)
        swaps = 0
    else:
        return [], 0

    # Perform the insertion sort algorithm
    for i in range(1, n):
        key = second_row[i]
        j = i - 1

        # Move elements of second_row[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < second_row[j]:
            second_row[j + 1] = second_row[j]
            j -= 1
            swaps += 1

        second_row[j + 1] = key

    return second_row, swaps

def selection_sort(matrix):
    """
    Sorts the third row of the matrix using the selection sort algorithm.
    Parameters:
        matrix: The unsorted matrix
    Returns:
        A tuple containing the sorted third row list and the number of swaps performed
    """
    # Get the third row of the matrix if it exists
    if matrix[2]:
        third_row = matrix[2]
        n = len(third_row)
        swaps = 0
    else:
        return [], 0

    # Perform the selection sort algorithm
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if third_row[j] < third_row[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element if they are different
        if min_idx != i:
            third_row[i], third_row[min_idx] = third_row[min_idx], third_row[i]
            swaps += 1

    return third_row, swaps


def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
        first_row (list of int): The first row of the matrix.
        second_row (list of int): The second row of the matrix.
        third_row (list of int): The third row of the matrix.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list