def trib(k):
    """
    The tribonacci sequence is a modified version of the Fibonacci sequence where each number is the sum of the three preceding numbers.
    :return: the k-th tribonacci number
    """
    return _trib(k, dict())


def _trib(k, memo):
    """
    Helper function for tribonacci sequence
    :return: the k-th tribonacci number
,    """
    if k == 1 or k == 2:
        return 0
    elif k == 3:
        return 1
    if k in memo:
        return memo[k]

    # store the result in the memo
    memo[k] = _trib(k - 1, memo) + _trib(k - 2, memo) + _trib(k - 3, memo)
    return memo[k]
