#python3


def max_pairwise_product(numbers):
    numbers.sort(reverse=True)
    max_number = numbers[0]
    second_number = numbers[1]
    n_max = second_number * max_number
    print(n_max)


if __name__ == '__main__':
    a = int(input())
    b = input().split()
    b1 = [int(item) for item in b]
    max_pairwise_product(b1)