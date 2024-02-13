class Animal:
    """
    Represents an animal with a name and species.

    Attributes:
    - name (str): The name of the animal.
    - species (str): The species of the animal.

    Methods:
    - __init__(name, species): Initializes an instance of the Animal class.
    - __repr__(): Returns a string representation of the Animal object.
    - make_sound(sound): Prints the sound made by the animal.
    """
    def __init__(self, name, species):
        """
        Initializes an instance of the Animal class.

        Parameters:
        - name (str): The name of the animal.
        - species (str): The species of the animal.
        """
        self.name = name
        self.species = species

    def __repr__(self):
        """
        Returns a string representation of the Animal object.
        """
        return f'{self.name} is a {self.species}'

    def make_sound(self, sound):
        """
        Prints the sound made by the animal.

        Parameters:
        - sound (str): The sound made by the animal.
        """
        print(f'This animal says {sound}')


class Cat(Animal):
    """
    Represents a cat, which is a type of animal.

    Inherits from the Animal class.

    Attributes:
    - breed (str): The breed of the cat.
    - toy (str): The toy with which the cat plays.

    Methods:
    - __init__(name, species, breed, toy): Initializes an instance of the Cat class.
    - play(): Prints a message indicating the cat is playing with its toy.
    """
    def __init__(self, name, species, breed, toy):
        """
        Initializes an instance of the Cat class.

        Parameters:
        - name (str): The name of the cat.
        - species (str): The species of the cat.
        - breed (str): The breed of the cat.
        - toy (str): The toy with which the cat plays.
        """
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

    def play(self):
        """
        Prints a message indicating the cat is playing with its toy.
        """
        print(f'{self.name} plays with {self.toy}')


# Example usage:
leo = Cat('Leo', 'Cat', 'Toy Pom', 'ball')
print(leo)  # Output: Leo is a Cat
leo.make_sound('meow')  # Output: This animal says meow
leo.play()  # Output: Leo plays with ball

