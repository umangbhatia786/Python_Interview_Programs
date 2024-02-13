# File: inheritance3.py

class Aquatic:
    """
    A class representing aquatic animals.
    """

    def __init__(self, name):
        """
        Initialize an Aquatic object with a name.
        """
        self.name = name

    def swim(self):
        """
        Return a string indicating the aquatic animal is swimming.
        """
        return f'{self.name} is swimming'
    
    def greet(self):
        """
        Return a greeting specific to aquatic animals.
        """
        return f'I am {self.name} of the sea.'
    

class Ambulatory:
    """
    A class representing land animals.
    """

    def __init__(self, name):
        """
        Initialize an Ambulatory object with a name.
        """
        self.name = name

    def walk(self):
        """
        Return a string indicating the land animal is walking.
        """
        return f'{self.name} is walking.'
    
    def greet(self):
        """
        Return a greeting specific to land animals.
        """
        return f'I am {self.name} of the land.'

class Penguin(Ambulatory, Aquatic):
    """
    A class representing a penguin, inheriting from Ambulatory and Aquatic classes.
    """

    def __init__(self, name):
        """
        Initialize a Penguin object with a name.
        """
        super().__init__(name)

    
captain_cook = Penguin('Captain Cook')
print(captain_cook.walk())
print(captain_cook.swim())
print(captain_cook.greet())