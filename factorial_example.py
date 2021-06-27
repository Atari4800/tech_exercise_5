def factorial_function(num):
    assert num >= 0. and type(num) is int, "The input is not recognized"

    if num == 0:
        return 1
    else:
        return num * factorial_function(num -1)
