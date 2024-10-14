def fizz_buzz(start, finish):
    """
    Prints numbers from start to finish, inclusive
    Replaces multiples of 3 (or contains a 3) with "fizz"
    Replaces multiples of 5 (or contains a 5) with "buzz"
    Replaces multiples of both with "fizzbuzz"

    Args:
        start (int): The first number.
        finish (int): The second number.
    """
    # Loop through numbers "start" to "finish"
    for i in range(start, finish + 1):
        # If the number is a multiple of 3 and 5
        if (i % 3 == 0 or "3" in str(i)) and (i % 5 == 0 or "5" in str(i)):
            print("fizzbuzz")
        # If the number is a multiple of 3 or contains 3
        elif i % 3 == 0 or "3" in str(i):
            print("fizz")
        # If the number is a multiple of 5 or contains 5
        elif i % 5 == 0 or "5" in str(i):
            print("buzz")
        # Otherwise just print the number
        else:
            print(i)
