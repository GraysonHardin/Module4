import unittest
from input_validation_assignment.input_validation.validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_average_first_number_negative(self):
        with self.assertRaises(ValueError):
            average(-90, 85, 95)


if __name__ == '__main__':
    unittest.main()

