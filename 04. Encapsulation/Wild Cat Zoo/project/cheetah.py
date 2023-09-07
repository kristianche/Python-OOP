from project.animal import Animal


class Cheetah(Animal):

    money_for_care = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Cheetah.money_for_care)