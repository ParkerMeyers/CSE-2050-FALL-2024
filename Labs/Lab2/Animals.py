class Animal:
    """
    A class representing an animal.
    """

    def __init__(self, name, species="animal", sound="hi"):
        """
        Initializes an Animal object with a name, species, and sound.
        :param name: The name of the animal
        :param species: The species of the animal
        :param sound: The sound the animal makes
        """
        self.name = name
        self.species = species
        self.sound = sound

    def __repr__(self):
        return f"Animal({self.name}, {self.species}, {self.sound})"

    def speak(self):
        return f"{self.name}, a {self.species}, says {self.sound}!"


class Dog(Animal):
    def __init__(self, name, is_good_boy=True):
        super().__init__(name, "dog", "ruff")
        self.is_good_boy = is_good_boy

    def __repr__(self):
        return f"Dog({self.name})"


class Cat(Animal):
    def __repr__(self):
        return f"Cat({self.name}, {self.species}, {self.sound})"
