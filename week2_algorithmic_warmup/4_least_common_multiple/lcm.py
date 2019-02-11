# Uses python3


def lcm_fast(a, b):
    multiplied = a * b
    if a == 1 or b == 1:
        print(max(a, b))
    else:
        while True:
            if a == 0 or b == 0:
                maximum = max(a, b)
                lcm = int(multiplied / maximum)
                print(lcm)
                break
            else:
                if a > b:
                    a = a - b
                else:
                    b = b - a


if __name__ == '__main__':
    a, b = map(int, input().split())
    lcm_fast(a, b)

