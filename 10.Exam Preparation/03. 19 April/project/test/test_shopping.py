from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Bravo", 100)

    def test_init(self):
        self.assertEqual("Bravo", self.shopping_cart.shop_name)
        self.assertEqual(100, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_valid_shop_name(self):
        self.shopping_cart.shop_name = "Bravo"
        self.assertEqual("Bravo", self.shopping_cart.shop_name)

    def test_invalid_shop_name_not_only_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Bravo0999"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_invalid_shop_name_not_first_capital(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "bravo"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_valid(self):
        result = self.shopping_cart.add_to_cart("Mlqko", 3.20)
        self.assertEqual(self.shopping_cart.products, {"Mlqko": 3.20})
        self.assertEqual("Mlqko product was successfully added to the cart!", result)

    def test_add_to_cart_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_cart.add_to_cart("Mlqko", 333.20)

        self.assertEqual("Product Mlqko cost too much!", str(ex.exception))

    def test_remove_from_cart_valid(self):
        self.shopping_cart.add_to_cart("Mlqko", 3.20)
        result = self.shopping_cart.remove_from_cart("Mlqko")

        self.assertEqual(self.shopping_cart.products, {})
        self.assertEqual(result, "Product Mlqko was successfully removed from the cart!")

    def test_remove_from_cart_invalid(self):
        self.shopping_cart.add_to_cart("Mlqko", 3.20)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Hlqb")

        self.assertEqual(str(ve.exception), "No product with name Hlqb in the cart!")

    def test_add(self):
        first = ShoppingCart('Test', 200)
        first.add_to_cart('from_first', 1)
        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)
        merged = first.__add__(second)
        self.assertEqual('TestSecondTest', merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_valid(self):
        self.shopping_cart.add_to_cart("Mlqko", 3.20)
        self.shopping_cart.add_to_cart("Hlqb", 6.80)
        result = self.shopping_cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 10.00lv.", result)

    def test_buy_products_invalid(self):
        self.shopping_cart.add_to_cart("Mqlko", 80.20)
        self.shopping_cart.add_to_cart("Hlqb", 56.80)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 37.00lv!", str(ve.exception))


if __name__ == "__main__":
    main()