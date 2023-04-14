from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON_PRIVATE_BOOTH = 3.50

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * PrivateBooth.PRICE_PER_PERSON_PRIVATE_BOOTH
        self.is_reserved = True