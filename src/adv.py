from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
     'outside':  Room("Outside Cave Entrance",
                      
                      "North of you, the cave mount beckons", None, None, None, None),

     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
 
 passages run north and east.""", None, None, None, None),

     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
 into the darkness. Ahead to the north, a light flickers in

 the distance, but there is no way across the chasm.""", None, None, None, None),

     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
 to north. The smell of gold permeates the air. There's what looks to be an abandoned
 railway on the ground. It was probably used by miners.""", None, None, None, None),

     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
 chamber! Sadly, it has already been completely emptied by
 earlier adventurers. Maybe they missed something... The only exit is to the south.""", None, None, None, None),
 }


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Item List

items = {
    'key' : Item("key", "A strange looking key. I wonder what it goes to..."),
    'sword' : Item("sword", "A rusty longsword, but it's better than nothing..."),
    'ruby' : Item("ruby", "A shiny ruby. It's cut into a peculiar shape."),
    'goblet' : Item("goblet", "A golden goblet encrusted with jewels. This would fetch a pretty penny!")
}

room['foyer'].add_item('sword')
room['narrow'].add_item('key')
room['overlook'].add_item('goblet')
room['treasure'].add_item('ruby')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
new_player = Player("John Python", room["outside"])
current_inventory = new_player.get_inventory()

while True:
    print(F"Current room: {new_player.current_room.name}, Description: {new_player.current_room.description}")

    print("Go North     : n")
    print("Go South     : s")
    print("Go East      : e")
    print("Go West      : w")
    print("To search the room : search")
    print("To check inventory : i")
    print("To pick up an item : take <item-name>")
    print("To drop  an item : drop <item-name>")
    print("To Quit   : q")

    action = input("What would you like to do? : ")
    words = action.strip().lower().split(" ")
    
    if len(words) == 1:
         if action not in ["n", "s", "e", "w", "search", "i", "q"]:
             print("Enter valid action")
             continue

         if action == "q":
             print("Thanks for playing!")
             break

         if action == "i":
             if len(new_player.inventory) < 1:
                 print("You don't currently have any items.")
                 continue
             else:
                 print(F"You have {current_inventory} in your inventory.")
                 continue

         current_room = new_player.current_room

         room_items = current_room.get_items()
         
         if action == "search":
             if len(room_items) < 1:
                 print("You didn't find anything.")
                 continue
             else:
                 print(F"You found a {room_items}. Maybe you should take something with you.")
                 continue

         if action == "n":
             if current_room.n_to is None:
                 print("You can't move North from here.")
                 continue
             else:
                 new_player.current_room = current_room.n_to

         elif action == "s":
             if current_room.s_to is None:
                 print("You can't move South from here.")
                 continue
             else:
                 new_player.current_room = current_room.s_to

         elif action == "e":
             if current_room.e_to is None:
                 print("You can't move East from here.")
                 continue
             else:
                 new_player.current_room = current_room.e_to


         elif action == "w":
             if current_room.w_to is None:
                 print("You can't move West from here.")
                 continue
             else:
                 new_player.current_room = current_room.w_to
                 
    elif len(words) == 2:
         if words[0] == "take":
             if words[1] not in new_player.current_room.get_items():
                 print(F"You don't see a {words[1]} in this room.")
                 continue
             else:
                 items[F"{words[1]}"].on_take()
                 new_player.current_room.take_item(words[1])
                 new_player.take_item(words[1])
                 
         elif words[0] =="drop":
             if words[1] not in current_inventory:
                print(F"You don't have a '{words[1]}', to drop.")
                continue
             else:
                items[F"{words[1]}"].on_drop()
                new_player.drop_item(words[1])
                new_player.current_room.add_item(words[1])
                
         else:
             print("Invalid action")
             continue

         if words[1] not in items.keys():
             print("Try to select a valid item.")
             continue

    else:
         print("Invalid action")
         continue 