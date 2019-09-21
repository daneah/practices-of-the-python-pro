from urllib.request import urlopen


def add_sales_tax(original_amount, country, region):
    sales_tax_rate = urlopen(f'https://tax-api.com/{country}/{region}').read().decode()
    return original_amount * float(sales_tax_rate)
