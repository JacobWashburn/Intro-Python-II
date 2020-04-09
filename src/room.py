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
