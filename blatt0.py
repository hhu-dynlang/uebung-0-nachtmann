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
    raise IndexError()
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


# print(is_palindrome("test"))
# print(is_palindrome("aaabbbaaa"))
# print_pascal([1, '\n', 1, 1, '\n', 1, 2, 1, '\n'])
print(flatten([1, 2, 3, [1, 2, 3], [4, 5, [6, 7, [8, 9]]]]))
