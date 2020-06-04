# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def get_inventory (self):
        return self.inventory

    def take_item (self, item):
        return self.inventory.append(item)

    def drop_item (self, item):
        return self.inventory.remove(item)

    def __repr__ (self):
        return (F"Name: {self.name}, Current Room: {self.current_room}, Inventory: {str(self.inventory)}")

    def __str__ (self):
        return (F"Name: {self.name}, Current Room: {self.current_room}, Inventory: {str(self.inventory)}")