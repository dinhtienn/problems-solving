from sys import stdin


def min_refills(distance, tank, stops):
    count = 0
    remainTank = tank
    remainDistance = distance

    if tank >= distance:
        return 0

    if tank < stops[0]:
        return -1

    for i in range(len(stops)):
        goneDistance = stops[i] - stops[i - 1] if i > 0 else stops[i]
        remainDistance -= goneDistance
        remainTank -= goneDistance
        distanceToGo = stops[i + 1] - \
            stops[i] if i < len(stops) - 1 else distance - stops[i]
        if remainTank < distanceToGo:
            if tank < distanceToGo:
                return -1

            remainTank = tank
            count += 1

    if remainTank >= remainDistance:
        return count

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
