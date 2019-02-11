#python3
import numpy as np


def lcm_fast(a, b):
    print(np.lcm(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    lcm_fast(a, b)