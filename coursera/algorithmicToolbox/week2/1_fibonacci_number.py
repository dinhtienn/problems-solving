def fibonacci(n):
    fibArray = [0, 1]

    for i in range(2, n + 1):
        fibArray.append(fibArray[i - 1] + fibArray[i - 2])

    return fibArray[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci(input_n))
