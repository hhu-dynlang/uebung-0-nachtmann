import random

from blatt0 import flatten, solve_equation, fizz_buzz, myint, mybin


def test_pascal():
    pass
    # assert gen_pascal(3) == [1, '\n', 1, 1, '\n', 1, 2, 1, '\n']


def test_flatten():
    assert flatten([[1, 2, 3], [4, 5]]) == [1, 2, 3, 4, 5]


def test_flatten_recursiv():
    assert flatten([1, 2, 3, [1, 2, 3], [4, 5, [6, 7, [8, 9]]]]) == [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# @pytest.mark.xfail(raises=Exception)
# def test_flatten_error():
#     flatten(1)


def test_solve_equation():
    x1, x2 = solve_equation(1, 4, 4)
    assert_equation(x1, x2, -2)


def test_solve_equation_2():
    x1, x2 = solve_equation(1, -3, -4)
    assert_equation(x1, x2, 4)
    assert_equation(x1, x2, -1)


def assert_equation(x1, x2, expected):
    assert x1 == expected or x2 == expected


def test_fizz_buzz():
    assert fizz_buzz(5) == [1, 2, 'Fizz', 4, 'Buzz']


def test_fizz_buzz_high():
    assert fizz_buzz(500)[-1] == 'Buzz'


def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)


def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i
