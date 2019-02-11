# Uses python3


def gcd_euclidean_fast(a, b):
    if a == 1 or b == 1:
        print(1)
    else:
        while True:
            if a == 0 or b == 0:
                print(max(a, b))
                break
            else:
                if a > b:
                    a = a - b
                else:
                    b = b - a


if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd_euclidean_fast(a, b)
