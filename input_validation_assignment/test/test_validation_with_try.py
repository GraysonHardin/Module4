import unittest
from unittest import mock
from input_validation_assignment.input_validation.validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average() == 90

    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
