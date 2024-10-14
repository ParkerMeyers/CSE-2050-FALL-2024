import string


def count_letters(data):
    """
    Counts how often individual letters appear in "data"

    Args:
        data (string): The string of data to count the letters in

    Returns:
        dict: letter:count pairs
    """
    pairs = {}
    # Loop through each letter in the string
    for letter in data:
        # Make sure all the letters are lowercase
        letter = letter.lower()
        # Check if the letter is an ascii character
        if letter not in string.ascii_lowercase:
            continue
        # If the letter already exists in the dict, increment it by one
        if letter in pairs:
            pairs[letter] += 1
        # If the letter does not exist in the dict, add it
        else:
            pairs[letter] = 1

    # Return the completed dict
    return pairs


# Test the function with the frost.txt file
if __name__ == '__main__':
    with open("res/frost.txt", "r") as file:
        data_frost = file.read()
        print(count_letters(data_frost))
