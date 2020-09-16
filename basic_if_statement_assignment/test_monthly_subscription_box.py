import unittest
from unittest.mock import patch

from basic_if_statement_assignment.monthly_subscription_box import membership


@patch('builtins.input')
@patch('builtins.print')
class MyTestCase(unittest.TestCase):

    def test_membership_platinum(self, mock_print, mock_input):
        mock_input.return_value = 'Platinum'

        membership()
        mock_print.assert_called_with('You have selected the Platinum which costs $60')

    def test_membership_gold(self, mock_print, mock_input):
        mock_input.return_value = 'Gold'

        membership()
        mock_print.assert_called_with('You have selected the Gold which costs $50')

    def test_membership_silver(self, mock_print, mock_input):
        mock_input.return_value = 'Silver'

        membership()
        mock_print.assert_called_with('You have selected the Silver which costs $40')

    def test_membership_bronze(self, mock_print, mock_input):
        mock_input.return_value = 'Bronze'

        membership()
        mock_print.assert_called_with('You have selected the Bronze which costs $30')

    def test_membership_free_trial(self, mock_print, mock_input):
        mock_input.return_value = 'Free Trial'

        membership()
        mock_print.assert_called_with('You have selected the Free Trial which is free!')


if __name__ == '__main__':
    unittest.main()
