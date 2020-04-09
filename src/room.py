# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, *args):
        self.name = name
        self.description = description
        self.n_to = args
        self.s_to = args
        self.e_to = args
        self.w_to = args
        self.items = {}

    def get_viable_directions(self):
        return {
            'north': self.n_to,
            'south': self.s_to,
            'east': self.e_to,
            'west': self.w_to
        }

    def add_item(self, item_id, item):
        self.items[item_id] = item

    def remove_item(self, item_id):
        del self.items[item_id]

    def remove_all_items(self):
        self.items.clear()


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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
