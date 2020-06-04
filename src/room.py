# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def get_items (self):
        return self.items

    def add_item (self, item):
        return self.items.append(item)

    def take_item (self, item):
        return self.items.remove(item)

    def __repr__ (self):
        return (F"Name: {self.name}, Description: {self.description}, Items: {str(self.items)}")

    def __str__ (self):
        return (F"Name: {self.name}, Description: {self.description}, Items: {str(self.items)}")