# Inheritance Module

This module contains classes that demonstrate inheritance in Python.

## Classes

### Animal
Represents an animal with a name and species.

- Methods:
  - `__init__(name, species)`: Initializes an instance of the Animal class.
  - `__repr__()`: Returns a string representation of the Animal object.
  - `make_sound(sound)`: Prints the sound made by the animal.

### Cat
Represents a cat, which is a type of animal.

- Inherits from: Animal
- Additional Attributes:
  - `breed (str)`: The breed of the cat.
  - `toy (str)`: The toy with which the cat plays.
- Additional Method:
  - `play()`: Prints a message indicating the cat is playing with its toy.

### User
Represents a user with a first name, last name, and age.

- Methods:
  - `__init__(first, last, age)`: Initializes a User object.
  - `__repr__()`: Returns a string representation of the User object.
  - `get_age()`: Get the age of the User.
  - `set_age(age)`: Set the age of the User.
  - `full_name()`: Get the full name of the User.

### Moderator
Represents a moderator, inheriting from User.

- Additional Attributes:
  - `community (str)`: The community the moderator belongs to.
- Additional Methods:
  - `display_active_moderators()`: Display the number of active moderators.
  - `remove_post()`: Remove a post from the Moderator's community.

## Examples

### Creating a Cat
```python
fluffy = Cat('Fluffy', 'Cat', 'Persian', 'feather toy')
print(fluffy)  # Output: Fluffy is a Cat
fluffy.play()  # Output: Fluffy plays with feather toy
```

### Creating a User and Moderator
```python
user1 = User('Alice', 'Smith', 30)
print(user1)  # Output: User with name: Alice Smith and age: 30

moderator1 = Moderator('Bob', 'Johnson', 45, 'Python Community')
print(moderator1)  # Output: User with name: Bob Johnson and age: 45 and community: Python Community
```

Feel free to expand on these examples and provide more details as needed in the README.md.
