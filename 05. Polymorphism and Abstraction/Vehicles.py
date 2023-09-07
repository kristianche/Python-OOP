from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Car.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95




