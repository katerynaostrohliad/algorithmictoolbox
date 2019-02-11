# Uses python3
import sys


def optimal_summands(n):
    summands = []
    number = 1
    while n > 0:
        if number <= n:
            if number + 1 <= n - number or n - number == 0:
                summands.append(number)
                n -= number
                number += 1
            else:
                number += 1

    return summands


if __name__ == '__main__':
    inp = sys.stdin.read()
    n = int(inp)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
