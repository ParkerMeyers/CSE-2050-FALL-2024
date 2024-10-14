import random
import sys
import time


def generate_lists(size):
    """
    This function generates two lists of random integers with length equal to size.
    Time complexity: O(n)
    :param size: the length of the lists
    :return: two lists of random integers
    """
    # Use random.sample to generate a list of random integers
    list1 = random.sample(range(1, sys.maxsize), size)
    list2 = random.sample(range(1, sys.maxsize), size)

    return list1, list2


def find_common(list1, list2):
    """
    Returning the number of common items between two lists without using Python collections
    Time complexity: O(n^2)
    :param list1: The first list of integers
    :param list2: The second list of integers
    :return: The number of common integers
    """
    common = []  # O(1)
    for i in list1:  # O(n)
        if i in list2:  # O(n)
            common.append(i)  # O(1)
    return len(common)  # Total: O(n^2)


def find_common_efficient(list1, list2):
    """
    Returning the number of common items between two lists using Python collections
    Time complexity:
    :param list1: The first list of integers
    :param list2: The second list of integers
    :return: The number of common integers
    """
    return len(list(set(list1) & set(list2)))  # Total: O(n)


def measure_time():
    """
    Measures the execution time of find_common and find_common_efficient for different list sizes:
    10, 100, 1000, 10000, 20000. Prints a table showing this.
    :return: None
    """
    # Use python built in time module to measure time
    print("Size\t|\tInefficient\t|\tEfficient\t|\tDifference")
    for size in [10, 100, 1000, 10000, 20000]:
        # Generate two lists
        list1, list2 = generate_lists(size)
        # Measure the time taken by the inefficient algorithm
        start_time = time.time()
        find_common(list1, list2)
        inefficient_time = time.time() - start_time
        # Measure the time taken by the efficient algorithm
        start_time = time.time()
        find_common_efficient(list1, list2)
        efficient_time = time.time() - start_time
        # Print the results
        print(f"{size}\t|\t{inefficient_time}\t|\t{efficient_time}\t|\t{inefficient_time - efficient_time}")


if __name__ == "__main__":
    measure_time()
