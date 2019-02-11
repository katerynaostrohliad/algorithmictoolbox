# Uses python3


def get_change(m):
    coins = (10, 5, 1)
    count = 0
    for item in coins:
        if m == 0:
            return count

        else:
            number = (min(item, m))
            div = int(m/item)
            m = m - div * number
            count += div
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
