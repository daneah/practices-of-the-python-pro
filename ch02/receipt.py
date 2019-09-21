# Importing a single name
from sales_tax import add_sales_tax  # <1>


def print_receipt():
    total = ...
    state = ...
    print(f'TOTAL: {total}')
    print(f'AFTER TAX: {add_sales_tax(total, state)}')  # <2>


# Importing the full module
import sales_tax


def print_receipt():
    total = ...
    locale = ...
    ...
    print(f'AFTER MILLAGE: {sales_tax.add_local_millage_tax(total, locale)}')
