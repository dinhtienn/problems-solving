# sum(fib(n)) = fib(n + 2) - 1
def fibonacci_sum(n):
    if n <= 1:
        return n

    limit = (n + 2) % 60  # pisanoLength(10) = 60
    previous = 0
    current = 1

    for _ in range(0, limit - 1):
        previous, current = current, (previous + current) % 10

    # safety guard if last digit of sum(fib(n + 2)) is 0
    if current != 0:
        return current - 1
    return 9


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
