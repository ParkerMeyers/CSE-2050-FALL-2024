from count_letters import count_letters

def is_anagram(word1, word2):
    """
    Determines whether two strings are anagrams and returns a boolean

    Args:
        word1 (string): The first string
        word2 (string): The second string

    Returns:
        boolean: If the first and second strings are anagrams
    """
    # Check if the count of the letters in word1 equals the count of the letters in word2
    if count_letters(word1) == count_letters(word2):
        return True
    else:
        return False
