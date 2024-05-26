from sys import stdin
from collections import namedtuple
import random

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    left = -1
    right = -1

    segments.sort()

    # write your code here
    for s in segments:
        if left == -1 or right == -1:
            left = s.start
            right = s.end
        elif s.start <= right:
            if s.start > left:
                left = s.start
            if s.end < right:
                right = s.end
        else:
            points.append(random.randint(left, right))
            left = s.start
            right = s.end

    points.append(random.randint(left, right))

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
