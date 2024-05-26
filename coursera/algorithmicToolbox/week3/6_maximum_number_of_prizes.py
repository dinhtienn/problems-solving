def optimal_summands(n):
    summands = []

    for i in range(1, n + 1):
        if n < i:
            if n != 0:
                lastNumber = summands[-1]
                del summands[-1]
                summands.append(lastNumber + n)
            break
        n -= i
        summands.append(i)

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
