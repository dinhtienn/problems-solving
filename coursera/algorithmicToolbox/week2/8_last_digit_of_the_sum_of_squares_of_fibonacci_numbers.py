# sum of squares of n-th fibonacci numbers
# (f0)^2 + (f1)^2 + (f2)^2 + (f3)^2 + (f4)^2 + .... + (fn)^2
# = fib(n) * fib(n + 1)

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    limit = n % 60  # pisano_length(10) = 60
    previous = 0
    current = 1

    for _ in range(0, limit):
        previous, current = current, (previous + current) % 10

    return (previous * current) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
