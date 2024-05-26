def fibonacci_partial_sum(from_, to):
    # uses the fibonacci property that last digit of the sum of 60 consecutive Fibonacci numbers is always 0
    m = from_ % 60  # pisanoLength(10) = 60
    n = to % 60

    if n <= m:
        n += 60

    current = 0
    _next = 1
    _sum = 0

    for i in range(n + 1):
        if i >= m:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
