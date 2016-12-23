import unittest
import sys
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_zero_value(self):
        formated_price = format_price('0')
        self.assertEqual(formated_price, '0')
        formated_price = format_price('0.00')
        self.assertEqual(formated_price, '0')

    def test_spaces(self):
        formated_price = format_price('1234567890')
        self.assertEqual(formated_price, '1 234 567 890')
        formated_price = format_price('1234')
        self.assertEqual(formated_price, '1 234')
        formated_price = format_price('123')
        self.assertEqual(formated_price, '123')

    def test_zeros_after_the_decimal_point(self):
        formated_price = format_price('1.10000')
        self.assertEqual(formated_price, '1.1')
        formated_price = format_price('1.0100')
        self.assertEqual(formated_price, '1.01')
        formated_price = format_price('0.01')
        self.assertEqual(formated_price, '0.01')


if __name__ == '__main__':
    unittest.main()
