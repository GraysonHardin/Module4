"""
Program: compound_expressions.py
Author: Grayson Hardin
Last date modified: 9/17/2020

Basic if-elif examples. Depending on what the variables are it will return which one is higher and lower.

"""


def range_of_variable():
    MAX = 10
    MIN = 0
    Y = -1
    X = 5

    if Y > MAX:
        print(Y, 'is greater than', MAX)

    if Y < MIN:
        print(Y, 'is less than', MIN)

    if MIN < X < MAX:
        print(X, 'is greater than', MIN, 'and less than', MAX)

    if MIN <= X < MAX:
        print(MIN, 'is less than or equal to', X, 'and', X, 'is less than', MAX)

    if MIN < X <= MAX:
        print(X, 'is greater than', MIN, 'and', X, 'is less than or equal to', MAX)


if __name__ == '__main__':
    range_of_variable()
