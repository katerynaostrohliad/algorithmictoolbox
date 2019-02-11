# Uses python3
import sys
from _operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = sorted(segments, key=attrgetter('end'))
    max_right = segments[0].end
    points.append(max_right)
    i = 1
    while i < len(segments):
        if max_right < segments[i].start:
            max_right = segments[i].end
            points.append(max_right)
        i += 1
    return points


if __name__ == '__main__':
    inp = sys.stdin.read()
    #inp = input()
    n, *data = map(int, inp.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
