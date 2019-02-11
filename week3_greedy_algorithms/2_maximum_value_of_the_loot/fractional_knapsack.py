# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    val_per_wei = [int(v)/int(w) for v, w in zip(values, weights)]
    val_per_wei, values, weights = zip(*sorted(zip(val_per_wei, values, weights), reverse=True))
    for ratio, val, wei in zip(val_per_wei, values, weights):
        if capacity == 0:
            return value
        else:
            num = (min(wei, capacity))
            capacity -= num
            wei -= num
            value += num * ratio

    return value


if __name__ == "__main__":
    #data = list(map(int, sys.stdin.read().split()))
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
