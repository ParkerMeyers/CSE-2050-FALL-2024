class Foo:
    """
    A simple class that has a name and profession, and can speak.
    """

    def __init__(self, name, profession):
        """
        Initializes a Foo object with a name and profession.
        :param name: the name of the Foo
        :param profession: the profession of the Foo
        """
        self.name = name
        self.profession = profession

    def __repr__(self):
        """
        :return: a string representation of the Foo object
        """
        return f"Foo({self.name}, {self.profession})"

    def speak(self):
        """
        :return: a string with the Foo object's name
        """
        return f"{self.name} says hello!"
