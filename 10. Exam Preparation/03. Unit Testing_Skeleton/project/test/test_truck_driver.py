from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTest(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Ivan", 1.20)

    def test_init(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(1.20, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_invalid_earned_money(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        self.assertEqual("Ivan went bankrupt.", str(ex.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Berlin", 600)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_invalid_cargo_offer(self):
        self.driver.available_cargos["Plovdiv"] = 40
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Plovdiv", 40)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_valid_cargo_offer(self):
        result = self.driver.add_cargo_offer("Plovdiv", 40)
        self.assertEqual("Cargo for 40 to Plovdiv was added as an offer.", result)
        self.assertEqual({"Plovdiv": 40}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("Plovdiv", 40)
        self.driver.add_cargo_offer("Sofia", 60)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, "Ivan is driving 60 to Sofia.")
        self.assertEqual(self.driver.earned_money, 72.0)
        self.assertEqual(self.driver.miles, 60)

    def test_drive_best_cargo_offer_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_eat(self):
        self.driver.earned_money = 200
        self.driver.eat(500)
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 160)

    def test_sleep(self):
        self.driver.earned_money = 200

        self.driver.sleep(2000)
        self.driver.sleep(3000)

        self.assertEqual(self.driver.earned_money, 110)

    def test_pump_gas(self):
        self.driver.earned_money = 1500

        self.driver.pump_gas(3000)
        self.driver.pump_gas(4500)

        self.assertEqual(self.driver.earned_money, 500)

    def test_repair_truck(self):
        self.driver.earned_money = 22500

        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(self.driver.earned_money, 7500)

    def test_repr(self):
        self.assertEqual("Ivan has 0 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()