def pisano_length(m):
    l = 1
    previousR = 0
    currentR = 1

    while True:
        previousR, currentR = currentR, (previousR + currentR) % m
        if previousR == 0 and currentR == 1:
            break
        l += 1

    return l


def huge_fibonacci(n, m):
    if n <= 1:
        return n

    limit = n % pisano_length(m)
    if limit <= 0:
        return 0

    previous = 0
    current = 1

    for _ in range(limit - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(huge_fibonacci(n, m))
