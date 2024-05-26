def change(money):
    denominations = [10, 5, 1]
    coins = 0

    for i in range(len(denominations)):
        coins += money // denominations[i]
        money = money % denominations[i]

        if money == 0:
            break

    return coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
