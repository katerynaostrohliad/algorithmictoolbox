# Uses python3


def get_fibonacci_last_digit_fast(n):
    fibonacci = list()
    for index in range(n + 1):
        if index <= 1:
            fibonacci.append(index)
        else:
            first = list(str(fibonacci[1]))
            zero = list(str(fibonacci[0]))
            last_digit = int(first[-1]) + int(zero[-1])
            fibonacci.append(last_digit)
            del fibonacci[0]
    new_number = list(str(fibonacci[-1]))
    print(new_number[-1])


if __name__ == '__main__':
    n = int(input())
    get_fibonacci_last_digit_fast(n)
