from math import sqrt


def is_palindrome(word):
    i = 0
    for s in reversed(word):
        if s != word[i]:
            return False
        i += 1
    return True


def gen_pascal(n):
    for i in range(0, n):
        print(i)


def print_pascal(n):
    for i in n:
        print(i)


def flatten(not_flat):
    if not isinstance(not_flat, list):
        raise Exception()
    result = []
    for l in not_flat:
        if isinstance(l, list):
            for i in l:
                if isinstance(i, list):
                    for j in flatten(i):
                        result.append(j)
                else:
                    result.append(i)

        else:
            result.append(l)
    return result


def solve_equation(a, b, c):
    p = b / a
    q = c / a
    x1 = -(p / 2) + sqrt((p / 2) ** 2 - q)
    x2 = -(p / 2) - sqrt((p / 2) ** 2 - q)
    return x1, x2


def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("Fizz Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
        print(result[-1])
    return result


def mybin(x):
    result = ""
    a = x
    while a != 0:
        x = a
        a = int(x / 2)
        b = x % 2
        result = str(b) + result
    return "0b" + result


def myint(x):
    x = x[2:]
    result = 0
    count = 0
    for i in reversed(x):
        if i == "1":
            result += 2 ** count
        print(result)
        count += 1
    return result


# print(is_palindrome("test"))
# print(is_palindrome("aaabbbaaa"))
# print_pascal([1, '\n', 1, 1, '\n', 1, 2, 1, '\n'])
# print(flatten([1, 2, 3, [1, 2, 3], [4, 5, [6, 7, [8, 9]]]]))
