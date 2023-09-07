from project.food import Food


class Fruit(Food):

    def __init__(self, name, expiration_data):
        super().__init__(expiration_data)
        self.name = name