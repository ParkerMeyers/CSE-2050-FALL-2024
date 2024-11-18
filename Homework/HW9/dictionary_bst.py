class Node:
    """
    A class to represent a node in the tree.
    """

    def __init__(self, word, meaning):
        """
        Arguments:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """

    def __init__(self, entries: dict[str, str] | None = None):
        """
        Arguments:
            entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Arguments:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if self.root is None:
            self.root = Node(word, meaning)
        else:
            self._insert_recursive(self.root, word, meaning)

    def _insert_recursive(self, node, word, meaning):
        """
        A recursive helper function to insert a word into the tree.

        Arguments:
            node (Node): The current node.
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if word < node.word:
            if node.left is None:
                node.left = Node(word, meaning)
            else:
                self._insert_recursive(node.left, word, meaning)
        elif word > node.word:
            if node.right is None:
                node.right = Node(word, meaning)
            else:
                self._insert_recursive(node.right, word, meaning)
        else:
            node.meaning = meaning

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Arguments:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        """
        A recursive helper function to search for a word in the tree.

        Arguments:
            node (Node): The current node.
            word (str): The word to search for.

        Returns:
            str: The meaning of the word if found, else return None'
        """
        if node is None:
            return None
        if word < node.word:
            return self._search_recursive(node.left, word)
        elif word > node.word:
            return self._search_recursive(node.right, word)
        return node.meaning

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        result = []
        self._in_order_transversal(self.root, result)
        return result

    def _in_order_transversal(self, node, result):
        """
        A recursive helper function to transverse the tree in-order.

        Arguments:
            node (Node): The current node.
            result (list of tuple): List of tuples, each containing (word, meaning).
        """
        if node is not None:
            self._in_order_transversal(node.left, result)
            result.append((node.word, node.meaning))
            self._in_order_transversal(node.right, result)
