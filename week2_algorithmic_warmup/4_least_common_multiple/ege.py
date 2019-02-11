#python3


def computeGCD(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm_fast(a, b):
    multiplied = a * b
    lcm = int(multiplied // computeGCD(a, b))
    print(lcm)


if __name__ == '__main__':
    a, b = map(int, input().split())
    lcm_fast(a, b)
