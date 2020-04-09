from room import Room
from item import Item


def initialization():
    # Declare all items

    item = {
        1: Item('Axe', 'The axe of Doom!'),
        2: Item('Revolver', 'This revolver has been fired recently.'),
        3: Item('Shovel', 'A shovel that seems to have been discarded.'),
        4: Item('Coin', 'It\'s Gold!'),
        5: Item('Binoculars', 'Used to see across vast distances.'),
        6: Item('Torch', 'A torch to light the way.')
    }

    # Declare all the rooms

    room = {
        'outside': Room("Outside Cave Entrance",
                        "North of you, the cave mount beckons"),

        'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east."""),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

        'narrow': Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south."""),
    }

    # Link items to rooms

    room['outside'].add_item(1, item[1])
    room['foyer'].add_item(2, item[2])
    room['overlook'].add_item(5, item[5])
    room['narrow'].add_item(6, item[6])
    room['treasure'].add_item(3, item[3])
    room['treasure'].add_item(4, item[4])

    # Link rooms together

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

    return room['outside']
