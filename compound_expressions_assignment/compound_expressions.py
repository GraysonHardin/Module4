def range_of_variable():
    MAX = 10
    MIN = 0
    Y = -1
    X = 5

    if Y > MAX:
        print(Y, 'is greater than', MAX)

    elif Y < MIN:
        print(Y, 'is less than', MIN)

    if MIN < X < MAX:  # cannot is an "elif" otherwise it will not print.
        print(X, 'is greater than', MIN, 'and less than', MAX)

    if MIN <= X < MAX:
        print(X, 'is greater than or equal to', MIN, 'and', X, 'is less than', MAX)

    if MIN < X <= MAX:
        print(X, 'is greater than', MIN, 'and', X, 'is less than or equal to', MAX)


if __name__ == '__main__':
    range_of_variable()
