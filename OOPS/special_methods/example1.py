"""
This module defines a class called Human with special methods (__init__, __repr__, __len__, __add__, __mul__) and properties (first, last, age) to represent a human with first name, last name, and age. 
The class allows creating instances of humans, getting their full name and age, and performing operations like addition and multiplication.
"""

class Human:

    def __init__(self,first,last,age):
        self._first = first
        self._last = last
        self._age = age

    @property
    def first(self):
        return self._first
    
    @property
    def last(self):
        return self._last
    
    @property
    def age(self):
        return self._age
    
    @first.setter
    def first(self, first):
        self._first = first

    @last.setter
    def last(self, last):
        self._last = last

    @age.setter
    def age(self, age):
        self._age = age

    def __repr__(self) -> str:
        return f'Human named {self.first} {self.last} with age {self.age}'
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self._last, age=0)
        return 'You can\'t add that!'
    
    def __mul__(self,other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return 'Can\'t multiply!'