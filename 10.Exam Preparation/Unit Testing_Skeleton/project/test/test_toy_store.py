from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct__init(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_on_none_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "HotWheels")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_that_is_already_on_shelf_raises_exception(self):
        self.store.add_toy("A", "HotWheels")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "HotWheels")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_on_a_full_shelf_raises_exception(self):
        self.store.add_toy("A", "Doll")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "HotWheels")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully_returns_string(self):
        result = self.store.add_toy("A", "HotWheels")

        self.assertEqual("Toy:HotWheels placed successfully!", result)
        self.assertEqual("HotWheels", self.store.toy_shelf["A"])

    def test_remove_toy_on_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "HotWheels")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_on_non_existing_shelf_from_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "HotWheels")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_correct(self):
        self.store.toy_shelf["A"] = "HotWheels"
        result = self.store.remove_toy("A", "HotWheels")

        self.assertIsNone(self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:HotWheels successfully!", result)


if __name__ == '__main__':
    main()
