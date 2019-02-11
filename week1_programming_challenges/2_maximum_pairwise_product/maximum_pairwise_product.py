# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = [numbers[first] * numbers[second] for first in range(n) for second in range(first + 1, n)]
    maxi = max(max_product)
    return maxi


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
