from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    def __init__(self, name: str, kind: str, price: float):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight: int = 9
        super().__init__(self.name, self.kind, self.price, self.weight)

    def eating(self):
        self.weight += 3