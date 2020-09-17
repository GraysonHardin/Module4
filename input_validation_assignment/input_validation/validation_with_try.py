"""
Program: validation_with_try.py
Author: Grayson Hardin
Last date modified: 9/17/2020
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':
    average()
