from itertools import permutations


def revenue(price, click):
    return price * click


def max_dot_product(first_sequence, second_sequence):
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)

    return sum(map(revenue, first_sequence, second_sequence))


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
