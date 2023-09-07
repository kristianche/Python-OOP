from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON_OPEN_BOOTH = 2.50

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people):
        self.price_for_reservation = number_of_people * OpenBooth.PRICE_PER_PERSON_OPEN_BOOTH
        self.is_reserved = True

