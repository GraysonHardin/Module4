"""
Program: coupon_calculation.py
Author: Grayson Hardin
Last date modified:

This program emulates a shopping cart. Upon checking out, the user is given the two discounts: cash and percent discounts.
During the testing, I added additional tests to cover the price changes (i.e: an item that costs $29 has a shipping costs of $5.95 whereas an item that is $30 has a shipping of $7.95).
In addition to the extra testing, I added extra scenarios for the different cash and percent discounts to account for the various situations.

"""


def calculate_order(price, cash_coupon, percent_coupon):
    if price < 10:
        shipping_cost = 5.95
        return price_calculation(price, cash_coupon, percent_coupon, shipping_cost)

    elif 10 <= price <= 29:
        shipping_cost = 7.95
        return price_calculation(price, cash_coupon, percent_coupon, shipping_cost)

    elif 30 <= price <= 49:
        shipping_cost = 11.95
        return price_calculation(price, cash_coupon, percent_coupon, shipping_cost)

    elif price >= 50:
        shipping_cost = 0
        return price_calculation(price, cash_coupon, percent_coupon, shipping_cost)


def price_calculation(price, cash_coupon, percent_coupon, shipping):
    tax = 0.06
    if cash_coupon is None and percent_coupon is None:
        price_after_tax = price * tax + price
        price_after_shipping = price_after_tax + shipping
        return round(price_after_shipping, 2)

    elif cash_coupon is None:
        price_after_discount = price - (percent_coupon * price)
        price_after_tax = price_after_discount * tax + price_after_discount
        price_after_shipping = price_after_tax + shipping
        return round(price_after_shipping, 2)

    elif percent_coupon is None:
        price_after_cash_coupon = (price - cash_coupon)
        price_after_tax = price_after_cash_coupon * tax + price_after_cash_coupon
        price_after_shipping = price_after_tax + shipping
        return round(price_after_shipping, 2)

    else:
        price_after_cash_coupon = (price - cash_coupon)
        price_after_discount = price_after_cash_coupon - (percent_coupon * price_after_cash_coupon)
        price_after_tax = price_after_discount * tax + price_after_discount
        price_after_shipping = price_after_tax + shipping
        return round(price_after_shipping, 2)


if __name__ == '__main__':
    calculate_order()
