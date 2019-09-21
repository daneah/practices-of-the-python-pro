# Take 1
def add_sales_tax(total, tax_rate):
    return total * tax_rate


# Take 2
TAX_RATES_BY_STATE = {  # <1>
    'MI': 1.06,
    # ...
}

def add_sales_tax(total, state):
    return total * TAX_RATES_BY_STATE[state]  # <2>


# Take 3
TAX_RATES_BY_STATE = {
    'MI': 1.06,
    ...
}

def add_sales_tax(total, state):
    tax_rate = TAX_RATES_BY_STATE[state]  # <1>
    return total * tax_rate  # <2>