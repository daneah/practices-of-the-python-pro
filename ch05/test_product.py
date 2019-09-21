import unittest

from product import Product


class ProductTestCase(unittest.TestCase):
    def test_working(self):
        pass

    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')  # <1>
        expected_value = 'SHOES'  # <2>
        actual_value = small_black_shoes.transform_name_for_sku()  # <3>
        self.assertEqual(expected_value, actual_value)  # <4>
