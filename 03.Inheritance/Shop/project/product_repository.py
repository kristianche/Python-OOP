from typing import List
from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p}: {p.quantity}" for p in self.products])




