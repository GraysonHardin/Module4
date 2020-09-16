import unittest

from input_validation_assignment.input_validation.validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_average_first_number_negative(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_second_number_negative(self):
        with self.assertRaises(ValueError):
            average(90, -89, 78)




if __name__ == '__main__':
    unittest.main()
