class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f'There are curently {cls.active_users} active users'
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first,last,int(age))
    
    def __repr__(self):
        return f'User with name: {self.full_name()} and age: {self.get_age()}'
    
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age <= 0:
            raise ValueError('Age must be a positive value')
        self._age = age

    def full_name(self):
        return f'{self._first} {self._last}'
    
    def logout(self):
        User.active_users -= 1
        return f'{self.full_name()} has been logged out'
    
    def is_senior(self):
        return self.get_age() >= 65
    
    def get_initials(self):
        return f'{self._first[0]}.{self._last[0]}'


user1 = User.from_string('Umang,Bhatia,29')
print(user1)
print(user1.get_initials())
print(user1.full_name())
    

        