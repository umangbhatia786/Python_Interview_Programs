# This file defines classes User and Moderator for a user system with inheritance.

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        """Display the number of active users."""
        return f'There are currently {cls.active_users} active users'
    
    @classmethod
    def from_string(cls, data_str):
        """Create a User object from a string."""
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))
    
    def __repr__(self):
        """Return a string representation of the User object."""
        return f'User with name: {self.full_name()} and age: {self.get_age()}'
    
    def __init__(self, first, last, age):
        """Initialize a User object with first name, last name, and age."""
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1

    def get_age(self):
        """Get the age of the User."""
        return self._age
    
    def set_age(self, age):
        """Set the age of the User."""
        if age <= 0:
            raise ValueError('Age must be a positive value')
        self._age = age

    def full_name(self):
        """Get the full name of the User."""
        return f'{self._first} {self._last}'
    
    def logout(self):
        """Logout the User and update the active user count."""
        User.active_users -= 1
        return f'{self.full_name()} has been logged out'
    
    def is_senior(self):
        """Check if the User is a senior (age 65 or older)."""
        return self.get_age() >= 65
    
    def get_initials(self):
        """Get the initials of the User."""
        return f'{self._first[0]}.{self._last[0]}'


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        """Initialize a Moderator object with first name, last name, age, and community."""
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_moderators(cls):
        """Display the number of active moderators."""
        return f'There are currently {cls.total_mods} active moderators.'

    def __repr__(self):
        """Return a string representation of the Moderator object."""
        return f'User with name: {self.full_name()} and age: {self.get_age()} and community: {self.community}' 

    def remove_post(self):
        """Remove a post from the Moderator's community."""
        return f'{self.full_name()} removed a post from {self.community} community'
    
    def logout(self):
        """Logout the Moderator and update the active moderator count."""
        Moderator.total_mods -= 1
        return f'{self.full_name()} has been logged out'