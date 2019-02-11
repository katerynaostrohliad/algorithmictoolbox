#python3


def max_pairwise(numbers):
    first = len(numbers)
    list_of_multiplied = list()
    for x in numbers:
        if x != numbers[first]:
            multi = x * numbers[first]
            #if multi not in list_of_multiplied:
            list_of_multiplied.append(multi)
            if first > 1:
                first -= 1



    print(list_of_multiplied)


if __name__ == '__main__':
    a = int(input())
    b = input().split()
    b1 = [int(item) for item in b]
    (max_pairwise(b1))



