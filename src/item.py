class Item :
     def __init__ (self, name, description):
         self.name = name
         self.description = description

     def on_take (self):
         print(F"You picked up the {self.name}.")

     def on_drop (self):
         print(F"You have dropped the {self.name}.")

     def __repr__ (self):
         return (F"Name: {self.name}, Description: {self.description}")

     def __str__ (self):
         return (F"Name: {self.name}, Description: {self.description}")