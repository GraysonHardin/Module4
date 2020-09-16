"""
Program: average_scores.py
Author: Grayson Hardin
Last date modified: 9/10/2020
"""


def average():
    # Each variable down below (score1 - score3) will collect user input.
    score1 = int(input("Enter first number here:"))
    score2 = int(input("Enter second number here:"))
    score3 = int(input("Enter third number here:"))
    average_scores = (score1 + score2 + score3) / 3  # Here the we perform calculation on the previous variables.
    return average_scores


def main():
    # Like the previous, we collect another set of variables (last name, first name, and age)
    last_name = input("Enter last name:")
    first_name = input("Enter first name:")
    age = input("Enter age:")
    average_score = average()
    print(f'{last_name}, {first_name} age: {age} average grade: {average_score}') # return the values and format accordingly.


if __name__ == '__main__':
    main()
