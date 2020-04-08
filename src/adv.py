import textwrap
from player import Player
from room import Room

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


name = input('What is your name?: ')
player = Player(name, room['outside'])
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
wrapper = textwrap.TextWrapper(initial_indent = '~   ', subsequent_indent = '~   ')
text = wrapper.fill
opening_message = f'Welcome. {name}. '
print(text(opening_message))


def move_to(person, loop):
    if not loop:
        print('There is nothing in that direction. Please pick a new direction.')
    else:
        print(text(f'You are currently in the area: "{player.room.name}\n".'))
        print(text(f'{player.room.description}'))
    directions = person.room.get_viable_directions()
    named_directions = {
        'n': 'North',
        's': 'South',
        'e': 'East',
        'w': 'West'
    }
    for k, v in directions.items():
        if v:
            print(text(f'\nTo the {named_directions[k]} is the {v.name}.'))
    go = input('What direction to travel? [N][S][E][W] Quit[Q]:').lower()
    while go not in ('n', 'e', 's', 'w', 'q'):
        go = input('Please input a correct direction. [N][S][E][W] Quit[Q]:').lower()
    if go == 'q':
        return go
    for k, v in directions.items():
        if v and go == k:
            for i in room:
                if room[i].name == v.name:
                    person.room = room[i]
                    return go
    else:
        return False


stop = move_to(player, True)
while stop != "q":
    if not stop:
        stop = move_to(player, False)
    else:
        stop = move_to(player, True)
print('Good Bye!')
