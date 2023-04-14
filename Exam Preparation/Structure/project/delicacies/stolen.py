from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    STOLEN_PORTION = 250

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        super().__init__(self.name, Stolen.STOLEN_PORTION, self.price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."