from collections import defaultdict


class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))  # <1>

    def add_product(self, product, quantity=1):  # <2>
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, product, quantity=1):  # <3>
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] == 0:
            del self.products[sku]

        """
        To fix the bug:
        if self.products[sku]['quantity'] <= 0:
            del self.products[sku]
        """
