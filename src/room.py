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

    def get_viable_directions(self):
        return {
            'n': self.n_to,
            's': self.s_to,
            'e': self.e_to,
            'w': self.w_to
        }
