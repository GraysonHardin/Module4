"""
Program: monthly_subscription.py
Author: Grayson Hardin
Last date modified:

This program allows the user to select a membership type. Upon selecting, it will return the version they selected, the cost, and the benefits of the version.
As a bonus, I added an Else-Statement to handle incorrect inputs and it will force the user to enter a valid input.

"""


def membership():
    print("Please choose your monthly Programmer's Toolkit Subscription Service: Platinum, Gold, Silver, Bronze, and Free Trial. ")
    user_input = str(input())
    if user_input == 'Platinum':
        print("You have selected the Platinum which costs $60")

    elif user_input == 'Gold':
        print('You have selected the Gold which costs $50')

    elif user_input == 'Silver':
        print('You have selected the Silver which costs $40')

    elif user_input == 'Bronze':
        print('You have selected the Bronze which costs $30')

    elif user_input == 'Free Trial':
        print('You have selected the Free Trial which is free!')

    else:
        print('Error, please input a valid option. Try again.')
        return membership()


if __name__ == '__main__':
    membership()
