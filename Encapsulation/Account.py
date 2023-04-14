class Account:

    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin != self.__pin:
            return "Wrong pin"

        return self.__id

    def change_pin(self, old_pin: int, new_pin: int):
        if old_pin != self.__pin:
            return "Wrong pin"

        self.__pin = new_pin
        return "Pin changed"