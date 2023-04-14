from project.animal import Animal


class Lion(Animal):

    money_for_care = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Lion.money_for_care)