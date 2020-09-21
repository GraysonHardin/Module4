"""
Program: monthly_subscription.py
Author: Grayson Hardin
Last date modified: 9/21/2020

This program allows the user to select a membership type. Upon selecting, it will return the version they selected and the cost.
"""


def membership(user_input):
    # The user_input parameter is being used to gain input and the following statement on line 12 evaluates whether the input is equal to Platinum.
    if user_input == 'Platinum':
        return f'You have selected the Platinum which costs $60'

    elif user_input == 'Gold':
        return f'You have selected the Gold which costs $50'

    elif user_input == 'Silver':
        return f'You have selected the Silver which costs $40'

    elif user_input == 'Bronze':
        return f'You have selected the Bronze which costs $30'

    elif user_input == 'Free Trial':
        return f'You have selected the Free Trial which is free!'

    else:
        return f'You have entered an invalid value.'


def main():
    # Here the user input is stored.
    print("Please choose your monthly Programmer's Toolkit Subscription Service: Platinum, Gold, Silver, Bronze, and Free Trial. ")
    user_input = str(input("Enter service choice here: "))
    print(membership(user_input))


if __name__ == '__main__':
    main()
