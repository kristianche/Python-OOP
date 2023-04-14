class BaseRobot:

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip() or " " in value:
            raise ValueError("Robot name cannot be empty!")

        self.__name = value


robot = BaseRobot("Kris", "T", 1.50, 40)
robot.name = "Kr is"
print(robot.name)