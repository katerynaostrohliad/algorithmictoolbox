# Uses python3


def calc_fib(n):
    fibonacci = list()
    for index in range(n + 1):
        if index <= 1:
            fibonacci.append(index)
        else:
            fibonacci.append(fibonacci[index - 1] + fibonacci[index - 2])
    if n <= 1:
        print(fibonacci[n])
    else:
        print(fibonacci[n])


n = int(input())
calc_fib(n)
