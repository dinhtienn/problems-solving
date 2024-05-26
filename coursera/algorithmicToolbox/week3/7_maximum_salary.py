from functools import cmp_to_key


def custom_compare(a, b):
    a += b
    b += a

    for i in range(len(a)):
        if a[i] > b[i]:
            return -1
        elif a[i] < b[i]:
            return 1

    return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    sortedNumbers = [n for n in sorted(
        numbers, key=cmp_to_key(custom_compare))]

    return ''.join(sortedNumbers)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
