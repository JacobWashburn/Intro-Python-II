import textwrap

from input import travel, pickup, drop
from initialization import initialization
from player import Player

initial_room = initialization()

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


name = input('What is your name?: ')
while not name:
    name = input('Seriously? You don\'t have a name? Come on..... Give me your name: ')
player = Player(name, initial_room)

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
print(text('If at any time you need help just type: Help'))
print(text(''))

go = 'start'
while go not in ('q', 'quit', 'exit'):
    directions = player.room.get_viable_directions()
    if not go:
        go = go
    if go == 'start':
        print(text(f'You are currently in the area: "{player.room.name}\n".'))
    if go == 'moved':
        print(text(f'You have moved into the {player.room.name}'))
    if go == 'items':
        item = [v.name for i, v in player.items.items()]
        print(text(f'You picked up the {item.pop()}'))
    if go and go[0] == 'help':
        print('~   Game Options:\n')
        print('~   To examine the area you are in:           Look')
        print('~   To see a list of items you are holding:   Inventory')
        print('~   Available directions of travel:           N, S, E, W, North, South, East, West')
        print(
                '~   To move into a new area:                  Move, Head, Travel, Go, Walk + The direction you want to go.')
        print('~   To pick up something in a room:           Get, Take + The item you want to pick up.')
        print('~   To pick up everything in a room:          Get, Take + All.')
        print('~   To drop something you\'re holding:         Drop + The item you want to drop.')
        print('~   To drop everything you\'re holding:        Drop All')
        print('~   To exit the game:                         Exit, Quit, Q')
    if go and go[0] == 'inventory':
        inventory = [v.name for i, v in player.items.items()]
        if len(inventory):
            print(text(f'You are holding: {inventory}'))
        else:
            print(text(f'You aren\'t holding anything.'))
    if go and go[0] == 'look':
        print(text(f'You are in the {player.room.name}'))
        for thing in player.room.items:
            print(text(f'On the ground lies a {player.room.items[thing].name}. {player.room.items[thing].description}'))
        print(text(f'{player.room.description}'))
        for k, v in directions.items():
            if v:
                print(text(f'To the {k.capitalize()} is the {v.name}.'))
    x = input(': ').lower()
    go = x.split()
    if go and go[0] not in (
    'travel', 'go', 'head', 'walk', 'move', 'take', 'get', 'drop', 'q', 'look', 'inventory', 'help', 'exit', 'quit'):
        print(text(f'I don\'t know what {go[0]} means.'))
    if x in ('q', 'quit', 'exit'):
        go = x
    if go and go[0] in ('take', 'get'):
        go = pickup(player, go)
    if go and go[0] == 'drop':
        go = drop(player, go)
    if go and go[0] in ('go', 'travel', 'head', 'walk', 'move'):
        go = travel(player, go, directions)

print('Good Bye!')
