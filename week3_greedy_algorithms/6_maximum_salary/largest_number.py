#Uses python3

import sys


def is_greater_than(n, m):
    str1 = str(n) + str(m)
    str2 = str(m) + str(n)
    if int(str1) < int(str2):
        return 1
    else:
        return -1


def largest_number(a):
    result = list()
    while len(a) > 0:
        max_digit = 0
        for digit in a:
            if is_greater_than(digit, max_digit) == -1:
                max_digit = digit
        result.append(max_digit)
        a.remove(max_digit)
    res = "".join(result)
    print(res)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = inp.split()
    a = data[1:]
    largest_number(a)
