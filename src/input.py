def travel(person, user_input, directions):
    simple = {
        'n': directions['north'],
        's': directions['south'],
        'e': directions['east'],
        'w': directions['west']
    }
    if len(user_input) == 2:
        if user_input[1] not in ('n', 's', 'e', 'w', 'north', 'south', 'east', 'west'):
            print(f'{user_input[0].capitalize()} where?')
            return user_input
        for k, v in directions.items():
            if v and user_input[1] == k:
                person.room = directions[k]
                return 'moved'
        for i, e in simple.items():
            if e and user_input[1] == i:
                person.room = simple[i]
                return 'moved'
        else:
            print('There is nothing in that direction.')
            return user_input
    else:
        print(f'~   {user_input[0].capitalize()} where?')


def pickup(person, user_input):
    room_items = person.room.items
    person_items = [v.name.lower() for i, v in person.items.items()]
    if len(user_input) == 2:
        if user_input[1] == 'all':
            if len(person.room.items) > 0:
                person.add_all_items()
                return user_input[1]
            else:
                print('There\'s nothing in this area.')
        else:
            for i, v in room_items.items():
                if user_input[1] and v.name.lower() == user_input[1] and user_input[1] in [v.name.lower() for i, v in
                                                                                           person.room.items.items()]:
                    person.add_item(i, person.room.items[i])
                    return 'items'
                elif user_input[1] in person_items:
                    print(f'~   You already have the {user_input[1]}.')
                    return user_input
            else:
                print(f'~   Could not find {user_input[1]}.')
                return user_input
    else:
        print('Get what?')
        return user_input


def drop(person, user_input):
    if len(user_input) == 2:
        if len(person.items) > 0:
            if user_input[1] == 'all':
                print(f'~   You dropped: {[v.name for i, v in person.items.items()]}')
                person.remove_all_items()
                return user_input

            else:
                if user_input[1] in [v.name.lower() for i, v in person.items.items()]:
                    for i, v in person.items.items():
                        if user_input[1] == v.name.lower():
                            person.remove_item(i, person.items[i])
                            return user_input
                else:
                    print(f'~   You don\'t have the {user_input[1]}')
                    return user_input
        else:
            print('You\'re not holding anything.')
    else:
        print('Drop what?')
        return user_input


def help_text():
    return 'end of help'
