"""
Program: validation_with_try.py
Author: Grayson Hardin
Last date modified: 9/17/2020


This program (like last week's assignment) will collect user's name (first, last) and age, along with three scores.
This time however, the program will return a "Invalid input" message if a user enters a negative value (i.e; -95).
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3) / NUMBER_TESTS)


def main():
    last_name = input("Enter last name:")
    first_name = input("Enter first name:")
    age = input("Enter age:")
    score1 = int(input("Enter first number: "))
    score2 = int(input("Enter second number: "))
    score3 = int(input("Enter third number: "))
    try:
        average_score = average(score1, score2, score3)
        print(f'{last_name}, {first_name} age: {age} average grade: {average_score}')
    except:
        print('Invalid input. Please try again later.')


if __name__ == '__main__':
    main()
