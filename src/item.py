from room import *


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'


# Declare all items

item = {
    1: Item('Axe', 'The axe of Doom!'),
    2: Item('Revolver', 'This revolver has been fired recently.'),
    3: Item('Shovel', 'A shovel that seems to have been discarded.'),
    4: Item('Coin', 'It\'s Gold!'),
    5: Item('Binoculars', 'Used to see across vast distances.'),
    6: Item('Torch', 'A torch to light the way.')
}

# Link items to rooms

room['outside'].add_item(1, item[1])
room['foyer'].add_item(2, item[2])
room['overlook'].add_item(5, item[5])
room['narrow'].add_item(6, item[6])
room['treasure'].add_item(3, item[3])
room['treasure'].add_item(4, item[4])
