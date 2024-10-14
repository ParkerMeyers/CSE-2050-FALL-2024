import time


def time_function(func, args, n_trials=10):
    """
    Times the execution of a function with arguments.

    :param func: function to be executed
    :param args: arguments to pass to the function
    :param n_trials: number of times to run the function

    :return: the minimum time it took to execute the function for n_trials trials
    """

    minimum = float('inf')

    # Loop over the number of trials and return the minimum time
    for i in range(n_trials):
        start = time.time()
        func(args)
        end = time.time()
        # Calculate the time it took & update the minimum time if necessary
        elapsed = end - start
        if elapsed < minimum:
            minimum = elapsed
    return minimum


def time_function_flexible(func, args, n_trials=10):
    """
    Times the execution of a function with a tuple of arguments.

    :param func: function to be executed
    :param args: a tuple of an arbitrary number of arguments to be passed to f
    :param n_trials: number of times to run the function

    :return: the minimum time it took to execute the function for n_trials trials
    """

    minimum = float('inf')

    # Loop over the number of trials and return the minimum time
    for i in range(n_trials):
        start = time.time()
        # Unpack the arguments and call the function
        func(*args)
        end = time.time()
        # Calculate the time it took & update the minimum time if necessary
        elapsed = end - start
        if elapsed < minimum:
            minimum = elapsed
    return minimum


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2


    L1 = [i for i in range(10 ** 5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10 ** 6)]  # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1 * 1000))
    print("t(L2) = {:.3g} ms".format(t2 * 1000))
