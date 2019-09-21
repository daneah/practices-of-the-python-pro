import unittest
from unittest import mock

from tax import add_sales_tax


class SalesTaxTestCase(unittest.TestCase):
    @mock.patch('requests.get')  # <1>
    def test_get_sales_tax_returns_proper_value_from_api(self, mock_get):  # <2>
        test_tax_rate = 1.06
        tax_api_response = mock.Mock()  # <3>
        tax_api_response.text = str(test_tax_rate)  # <4>
        mock_get.return_value = tax_api_response  # <5>

        self.assertEqual(5 * test_tax_rate, add_sales_tax(5, 'USA', 'MI'))  # <6>
