from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GINGERBREAD_PORTION = 200

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        super().__init__(self.name, Gingerbread.GINGERBREAD_PORTION, self.price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."



