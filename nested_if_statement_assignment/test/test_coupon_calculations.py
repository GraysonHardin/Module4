import unittest
from nested_if_statement_assignment.store.coupon_calculations import calculate_order


class CouponTesting(unittest.TestCase):
    # Test Set 1
    def test_price_under_ten_with_five_coupon_with_ten_percent_discount(self):
        price = 8
        cash_coupon = 5
        percent_coupon = .10

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(8.81, actual)

    def test_price_under_ten_with_five_coupon_with_fifteen_discount(self):
        price = 8
        cash_coupon = 5
        percent_coupon = .15

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(8.65, actual)

    def test_price_under_ten_with_five_coupon_with_twenty_discount(self):
        price = 8
        cash_coupon = 5
        percent_coupon = .20

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(8.49, actual)

    def test_price_under_ten_with_ten_coupon_with_ten_discount(self):
        price = 8
        cash_coupon = 10
        percent_coupon = .10

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(4.04, actual)

    def test_price_under_ten_with_ten_coupon_with_fifteen_discount(self):
        price = 8
        cash_coupon = 10
        percent_coupon = .15

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(4.15, actual)

    def test_price_under_ten_with_ten_coupon_with_twenty_discount(self):
        price = 9
        cash_coupon = 10
        percent_coupon = .20

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(5.1, actual)


    # Test Set 2

    def test_price_ten_to_less_thirty_with_five_coupon_with_ten_discount(self):
        price = 10
        cash_coupon = 5
        percent_coupon = .10

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(12.72, actual)

    def test_price_ten_to_thirty_with_five_coupon_with_fifteen_discount(self):
        price = 10
        cash_coupon = 5
        percent_coupon = .15

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(12.46, actual)

    def test_price_ten_to_thirty_with_five_coupon_with_twenty_discount(self):
        price = 10
        cash_coupon = 5
        percent_coupon = .20

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(12.19, actual)

    def test_price_ten_to_thirty_with_ten_coupon_with_ten_discount(self):
        price = 10
        cash_coupon = 10
        percent_coupon = .10

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(7.95, actual)

    def test_price_ten_to_thirty_with_ten_coupon_with_fifteen_discount(self):
        price = 10
        cash_coupon = 10
        percent_coupon = .15

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(7.95, actual)

    def test_price_ten_to_thirty_with_ten_coupon_with_twenty_discount(self):
        price = 29
        cash_coupon = 10
        percent_coupon = .20

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(24.06, actual)


    # Test set 3
    def test_price_thirty_to_fifty_with_five_cash_coupon_with_ten_percent_discount(self):
        price = 30
        cash_coupon = 5
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(35.8, actual)

    def test_price_thirty_to_fifty_with_five_cash_coupon_with_fifteen_percent_discount(self):
        price = 30
        cash_coupon = 5
        percent_discount = .15

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(34.47, actual)

    def test_price_thirty_to_fifty_with_five_cash_coupon_with_twenty_percent_discount(self):
        price = 30
        cash_coupon = 5
        percent_discount = .20

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(33.15, actual)

    def test_price_thirty_to_fifty_with_ten_cash_coupon_with_ten_percent_discount(self):
        price = 30
        cash_coupon = 10
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(31.03, actual)

    def test_price_thirty_to_fifty_with_ten_cash_coupon_with_fifteen_percent_discount(self):
        price = 30
        cash_coupon = 10
        percent_discount = .15

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(29.97, actual)

    def test_price_thirty_to_fifty_with_ten_cash_coupon_with_twenty_percent_discount(self):
        price = 49
        cash_coupon = 10
        percent_discount = .20

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(45.02, actual)

    # Test set 4

    def test_price_fifty_and_above_with_five_cash_coupon_with_ten_percent_discount(self):
        price = 50
        cash_coupon = 5
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(42.93, actual)

    def test_price_fifty_and_above_with_five_cash_coupon_with_fifteen_percent_discount(self):
        price = 50
        cash_coupon = 5
        percent_discount = .15

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(40.55, actual)

    def test_price_fifty_and_above_with_five_cash_coupon_with_twenty_percent_discount(self):
        price = 50
        cash_coupon = 5
        percent_discount = .20

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(38.16, actual)

    def test_price_fifty_and_above_with_ten_cash_coupon_with_ten_percent_discount(self):
        price = 50
        cash_coupon = 10
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(38.16, actual)

    def test_price_fifty_and_above_with_ten_cash_coupon_with_fifteen_percent_discount(self):
        price = 50
        cash_coupon = 10
        percent_discount = .15

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(36.04, actual)

    def test_price_fifty_and_above_with_ten_cash_coupon_with_twenty_percent_discount(self):
        price = 100
        cash_coupon = 10
        percent_discount = .20

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(76.32, actual)

    def test_price_with_no_cash_coupon_or_percent_discount(self):
        price = 10
        cash_coupon = None
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(18.55, actual)

    def test_price_less_than_ten_with_no_coupons(self):
        price = 9
        cash_coupon = None
        percent_coupon = None

        actual = calculate_order(price, cash_coupon, percent_coupon)
        self.assertEqual(15.49, actual)

    def test_price_with_cash_coupon_but_no_percent_discount(self):
        price = 10
        cash_coupon = 5
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(13.25, actual)

    def test_price_with_no_cash_coupon_but_with_percent_discount(self):
        price = 10
        cash_coupon = None
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(17.49, actual)

    def test_price_when_ten_to_thirty_with_no_coupon(self):
        price = 11
        cash_coupon = None
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(19.61, actual)

    def test_price_when_ten_to_thirty_with_cash_but_no_percent_coupon(self):
        price = 11
        cash_coupon = 5
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(14.31, actual)

    def test_price_when_ten_to_thirty_with_no_cash_but_percent_coupon(self):
        price = 11
        cash_coupon = None
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(18.44, actual)


    def test_price_when_thirty_with_no_coupon(self):
        price = 30
        cash_coupon = None
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(43.75, actual)

    def test_price_when_thirty_with_cash_but_no_percent_coupon(self):
        price = 30
        cash_coupon = 5
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(38.45, actual)

    def test_price_when_thirty_with_no_cash_but_percent_coupon(self):
        price = 30
        cash_coupon = None
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(40.57, actual)

    def test_price_when_fifty_with_no_coupon(self):
        price = 50
        cash_coupon = None
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(53.0, actual)

    def test_price_when_fifty_with_cash_but_no_percent_coupon(self):
        price = 50
        cash_coupon = 5
        percent_discount = None

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(47.7, actual)

    def test_price_when_fifty_with_no_cash_but_percent_coupon(self):
        price = 50
        cash_coupon = None
        percent_discount = .10

        actual = calculate_order(price, cash_coupon, percent_discount)
        self.assertEqual(47.7, actual)



if __name__ == '__main__':
    unittest.main()
