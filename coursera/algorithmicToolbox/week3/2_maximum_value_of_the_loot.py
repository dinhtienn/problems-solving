from sys import stdin


def getPrice(value, weight):
    return value / weight


def optimal_value(capacity, weights, values):
    value = 0.

    prices = list(map(getPrice, values, weights))
    sortedZipList = sorted(zip(prices, weights, values),
                           key=None, reverse=True)

    prices = [p for p, _, _ in sortedZipList]
    weights = [w for _, w, _ in sortedZipList]
    values = [v for _, _, v in sortedZipList]

    for i in range(len(prices)):
        if capacity >= weights[i]:
            capacity -= weights[i]
            value += values[i]
        else:
            value += prices[i] * capacity
            break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
