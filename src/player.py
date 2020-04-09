# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = {}

    def add_item(self, item_id, item):
        self.items[item_id] = item
        self.room.remove_item(item_id)

    def add_all_items(self):
        print(f'~   You picked up: {[v.name for i, v in self.room.items.items()]}')
        for i, v in self.room.items.items():
            self.items[i] = v
        self.room.remove_all_items()

    def remove_item(self, item_id, item):
        del self.items[item_id]
        self.room.add_item(item_id, item)

    def remove_all_items(self):
        for i, v in self.items.items():
            self.room.add_item(i, v)
        self.items.clear()
