from blatt0 import flatten


# from blatt0 import fizz_buzz
# from blatt0 import solve_equation
# from blatt0 import myint, mybin


def test_pascal():
    pass
    # assert gen_pascal(3) == [1, '\n', 1, 1, '\n', 1, 2, 1, '\n']


def test_flatten():
    assert flatten([[1, 2, 3], [4, 5]]) == [1, 2, 3, 4, 5]


def test_flatten_recursiv():
    assert flatten([1, 2, 3, [1, 2, 3], [4, 5, [6, 7, [8, 9]]]]) == [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_fizz_buzz():
    pass  # TODO


def test_solve_equation():
    pass  # TODO

# def test_int_to_bin():
#     input = random.sample(range(1000), 10)
#     for x in input:
#         assert mybin(x) == bin(x)
#
#
# def test_bin_to_int():
#     input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
#     for i, bini in input:
#         assert myint(bini) == i

# TODO: more tests
